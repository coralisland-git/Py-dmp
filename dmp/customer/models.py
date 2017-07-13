import string
import random
import hashlib
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.utils.translation import ugettext_lazy as __


class Customer(AbstractBaseUser):
    """
    Customer model.
    """
    email = models.EmailField(__('email'), max_length=60, unique=True,
                              help_text=__('Required. 60 characters or fewer.'),
                              error_messages={
                                  'unique': __("A user with that email already exists."),
                              })
    is_active = models.BooleanField(__('is_active'), default=True)
    is_superuser = models.IntegerField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_username(self):
        return self.email

    objects = UserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)


class Profile(models.Model):
    """
    Customer's profile model.
    """
    user = models.ForeignKey(Customer)
    first_name = models.CharField(__('First name'), max_length=120, blank=True, null=True)
    last_name = models.CharField(__('Last name'), max_length=120, blank=True, null=True)
    company_name = models.CharField(__('Company name'), max_length=120, default=None)
    rs_username = models.CharField(__('Output datastorage username'), max_length=120, default=None, blank=True, null=True)
    rs_password = models.CharField(__('Output datastorage password'), max_length=120, default=None, blank=True, null=True)

    def password_generator(self, size=10, chars=string.ascii_uppercase + string.hexdigits):
        return "".join(random.SystemRandom().choice(chars) for _ in range(size))

    def rs_password_generator(self):
        return "md5{}".format(hashlib.md5("{}{}".format(self.rs_password, self.rs_username).encode('utf-8')).hexdigest())

    def username_generator(self):
        if '@' in self.user.email:
            return self.user.email.split('@')[0]
        return self.first_name
