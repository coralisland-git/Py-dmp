import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from django.conf import settings


def connect_to_rs():
    con = psycopg2.connect(dbname=settings.RS_CREDENTIALS.get("RSDEFAULTDATABASE"),
                           user=settings.RS_CREDENTIALS.get("RSUSER"),
                           host=settings.RS_CREDENTIALS.get("RSHOST"),
                           password=settings.RS_CREDENTIALS.get("RSPASSWORD"),
                           port=settings.RS_CREDENTIALS.get("RSPORT"))
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    return con, cur


def destroy_connection(cursor, connection):
    cursor.close()
    connection.close()


def upload_to_s3():
    default_iam_role = 'arn:aws:iam::114432149781:role/rs_role'
    bucket_path = 's3://amd-redshift-dump/dump-data/'
    "unload('select * from venue') to '{path}' iam_role '{role}'".format(path=bucket_path, role=default_iam_role)


def load_from_s3():
    pass