from customer.models import Customer
from django.core.management import BaseCommand
from django.db.utils import IntegrityError
from django.core import validators, exceptions


class Command(BaseCommand):

    # Show this when the user types help
    help = "Add new user for project. You will be prompted to enter valid email and password."

    def handle(self, *args, **options):
        email = input('Set email: ')
        password = input('Set password: ')
        try:
            validators.validate_email(email)
        except exceptions.ValidationError:
            print("Enter valid email address.")
        try:
            customer = Customer(email=email)
            customer.set_password(password)
            customer.save()
        except IntegrityError:
            print("User already exists.")







