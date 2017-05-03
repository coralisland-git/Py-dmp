from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.utils.translation import ugettext_lazy as _


class Customer(AbstractBaseUser):
    """
    Customer model.
    """
    email = models.EmailField(_('email'), max_length=60, unique=True,
                              help_text=_('Required. 60 characters or fewer.'),
                              error_messages={
                                  'unique': _("A user with that email already exists."),
                              })
    is_active = models.BooleanField(_('is_active'), default=True)
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
