import os
from django.db import models
from .models import DataSource


class ZendeskDataSource(DataSource):
    data_source = models.OneToOneField(DataSource)
    login_url = models.CharField('Login URL', max_length=255)
    username = models.CharField('Username', max_length=255)
    password = models.CharField('Password', max_length=255)
    target = models.CharField('Source target type', max_length=255)

    class Meta:
        verbose_name = 'Zendesk Data source'
        verbose_name_plural = 'Zendesk Data sources'

    def create_config_file(self):
        pass

    def update_config_file(self):
        pass

