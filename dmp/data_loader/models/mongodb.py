from django.db import models
from .models import DataSource


class MongoDBDataSource(DataSource):
    data_source = models.OneToOneField(DataSource)
    uri = models.CharField('URI', max_length=255)
    hosts = models.CharField('Hosts', max_length=255)
    port = models.CharField('Port', max_length=255)
    username = models.CharField('Username', max_length=255)
    password = models.CharField('Password', max_length=255)
    database = models.CharField('Database', max_length=255)

    class Meta:
        verbose_name = 'MongoDB Data source'
        verbose_name_plural = 'MongoDB Data sources'

    def create_config_file(self):
        pass

    def update_config_file(self):
        pass

