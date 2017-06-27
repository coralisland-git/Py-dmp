import os
from django.db import models
from .models import DataSource


class SalesforceDataSource(DataSource):
    data_source = models.OneToOneField(DataSource)
    username = models.CharField('Username', max_length=255)
    password = models.CharField('Password', max_length=255)
    endpoint = models.CharField('Login endpoint', max_length=255)
    sf_object = models.CharField('API object name', max_length=255)

    class Meta:
        verbose_name = 'Salesforce Data source'
        verbose_name_plural = 'Salesforce Data sources'


    def create_config_file(self):
        pass

    def update_config_file(self):
        pass

