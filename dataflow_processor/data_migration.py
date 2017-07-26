import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from django.conf import settings
import time

# IAM user role for RS management (Note: this role must be added to 'IAM roles' section
# for both source and destination RS clusters)
s3_access_params = {
    'default_iam_role': 'arn:aws:iam::114432149781:role/rs_role',
    'bucket_path': 's3://amd-redshift-dump/dump-data/'
}

source_credentials = {'dbname': 'dmp',
                      'user': settings.RS_CREDENTIALS.get("RSUSER"),
                      'host': 'dmp-redshift.chjsswbt7mp7.eu-central-1.redshift.amazonaws.com',
                      'password': settings.RS_CREDENTIALS.get("RSPASSWORD"),
                      'port': settings.RS_CREDENTIALS.get("RSPORT")}

destination_credentials = {'dbname': 'dmp',
                           'user': settings.RS_CREDENTIALS.get("RSUSER"),
                           'host': settings.RS_CREDENTIALS.get("RSHOST"),
                           'password': settings.RS_CREDENTIALS.get("RSPASSWORD"),
                           'port': settings.RS_CREDENTIALS.get("RSPORT")}


def connect_to_rs(credentials):
    con = psycopg2.connect(**credentials)
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    return con, cur


def destroy_connection(cursor, connection):
    cursor.close()
    connection.close()


def get_table_names():
    con, cur = connect_to_rs(source_credentials)
    cur.execute("SELECT DISTINCT tablename FROM pg_table_def WHERE schemaname = 'public' ORDER BY tablename;")
    table_names = [row[0] for row in cur]
    destroy_connection(cur, con)
    return table_names


def unload_to_s3(cursor, table_name):
    cursor.execute("unload('select * from {table_name}') to '{path}/{table_name}' iam_role '{role}' ALLOWOVERWRITE DELIMITER ';' ;".format(
            table_name=table_name,
            path=s3_access_params.get('bucket_path'),
            role=s3_access_params.get('default_iam_role')))


def copy_from_s3(cursor, table_name):
    cursor.execute("copy {table_name} from '{path}/{table_name}' iam_role '{role}' DELIMITER ';' NULL AS 'null_string' ESCAPE FILLRECORD;".format(
        table_name=table_name,
        path=s3_access_params.get('bucket_path'),
        role=s3_access_params.get('default_iam_role')))


def migrate_data(tables_list=None):

    # Migrate data from between two RS clusters.
    # Note: Tables structure must be dumped from source cluster
    # and uploaded into destination cluster (with pg_dump tool or created manually)
    # before data migration.

    # Set connection to source and destination RS clusters
    s_con, s_cur = connect_to_rs(source_credentials)
    d_con, d_cur = connect_to_rs(destination_credentials)

    if not tables_list:
        tables_list = get_table_names()

    # Unload and copy data for each table available
    for table in tables_list:
        # dest_cur.execute('delete FROM {table}'.format(table=table))
            # Copy tables with data from RS cluster to S3 pre-created intermediate bucket
            unload_to_s3(s_cur, table)
            time.sleep(5)
            # Upload tables with data from S3 to RS
            copy_from_s3(d_cur, table)

    destroy_connection(s_cur, s_con)
    destroy_connection(d_cur, d_con)


