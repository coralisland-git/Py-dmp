from customer.models import Customer, Profile
from django.core.management import BaseCommand
from django.db.utils import IntegrityError
from django.core import validators, exceptions
from django.db import transaction
from django.conf import settings
import psycopg2
from psycopg2 import sql
import hashlib
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class Command(BaseCommand):

    help = "Add new user for project. You will be prompted to enter valid email, password and company name."

    def handle(self, *args, **options):
        email = input('Set email: ')
        password = input('Set password: ')
        company_name = input('Company name: ')
        if not email or not password or not company_name:
            raise ValueError('Please, set correct input values.')
        try:
            validators.validate_email(email)
        except exceptions.ValidationError:
            print("Enter valid email address.")
        try:
            with transaction.atomic():

                # create user from input info
                email = email.lower()
                customer = Customer(email=email)
                customer.set_password(password)
                customer.save()

                # create User's profile and set all needed info regarding redshift output storage
                profile, created = Profile.objects.get_or_create(user=customer, defaults={"company_name": company_name})
                profile.rs_username = profile.username_generator()
                profile.rs_password = profile.password_generator()
                profile.save()

                # prepare DB in redshift output storage for newly created user
                self.prepare_rs_db(user_info=profile)
        except IntegrityError:
            print("User or profile entry already exists.")

    def prepare_rs_db(self, user_info):
        """
        create separated database for user
        :param user_info: user information required to set RS database name and user access credentials
        :return:
        """
        default_group_name = 'dmp_users'
        db_name = user_info.company_name

        # set connection to default rs database with root user's credentials
        # credentials stored in settings.py file
        con = psycopg2.connect(dbname=settings.RS_CREDENTIALS.get("RSDEFAULTDATABASE"),
                               user=settings.RS_CREDENTIALS.get("RSUSER"),
                               host=settings.RS_CREDENTIALS.get("RSHOST"),
                               password=settings.RS_CREDENTIALS.get("RSPASSWORD"),
                               port=settings.RS_CREDENTIALS.get("RSPORT"))
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()

        # check if database already created (if present in the list of RS host's database names)
        # and create if not exists
        cur.execute("SELECT datname FROM pg_database_info;")
        some_list = [row[0] for row in cur]
        not_exists = not cur or db_name not in some_list
        if not_exists:
            cur.execute("CREATE DATABASE {};".format(db_name))

        # create new user group for customers if not exists already
        try:
            cur.execute("CREATE GROUP {};".format(default_group_name))
        except psycopg2.ProgrammingError:
            pass

        # create user in customers group and new schema associated to user
        cur.execute("CREATE USER {} IN GROUP {} PASSWORD '{}';".format(user_info.rs_username,
                                                                       default_group_name,
                                                                       user_info.rs_password_generator()))


        # reset access rules from default and grant privileges to user on his database and associated schema
        cur.execute("REVOKE ALL ON DATABASE {} FROM public;".format(user_info.company_name))
        cur.execute("GRANT ALL PRIVILEGES ON DATABASE {} TO {};".format(db_name,
                                                                        user_info.rs_username,
                                                                        user_info.company_name))
        cur.close()
        con.close()

        # set connection to newly created rs database with root user's credentials
        con = psycopg2.connect(dbname=user_info.company_name,
                               user=settings.RS_CREDENTIALS.get("RSUSER"),
                               host=settings.RS_CREDENTIALS.get("RSHOST"),
                               password=settings.RS_CREDENTIALS.get("RSPASSWORD"),
                               port=settings.RS_CREDENTIALS.get("RSPORT"))
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()

        cur.execute("CREATE SCHEMA IF NOT EXISTS {};".format(user_info.rs_username))
        cur.execute("GRANT ALL PRIVILEGES ON SCHEMA {} TO {};".format(user_info.rs_username,
                                                                      user_info.rs_username))
        cur.close()
        con.close()







