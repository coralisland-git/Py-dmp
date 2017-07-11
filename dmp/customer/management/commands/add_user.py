from customer.models import Customer, Profile
from django.core.management import BaseCommand
from django.db.utils import IntegrityError
from django.core import validators, exceptions
from django.db import transaction


@transaction.atomic()
class Command(BaseCommand):

    # Show this when the user types help
    help = "Add new user for project. You will be prompted to enter valid email and password."

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
            customer = Customer(email=email)
            customer.set_password(password)
            customer.save()
            Profile.objects.get_or_create(user=customer, defaults={"company_name": company_name})
        except IntegrityError:
            print("User already exists.")








