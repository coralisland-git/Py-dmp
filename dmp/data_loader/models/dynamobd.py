import os
from django.db import models
from .models import DataSource


class DynamoDBDataSource(DataSource):
    data_source = models.OneToOneField(DataSource)
    host = models.CharField('Host', max_length=255)
    port = models.CharField('Port', max_length=255)
    access_key = models.CharField('Access key', max_length=255)
    secret_key = models.CharField('Secret key', max_length=255)
    database = models.CharField('Database name', max_length=255)
    region = models.CharField('Region name', max_length=255)
    endpoint = models.CharField('Endpoint URl', max_length=255)
    table = models.CharField('Table name', max_length=255)

    class Meta:
        verbose_name = 'DynamoDB Data source'
        verbose_name_plural = 'DynamoDB Data sources'

    def create_config_file(self):
        pass

    def update_config_file(self):
        pass

