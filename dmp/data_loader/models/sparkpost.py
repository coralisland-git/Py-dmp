import os
from django.db import models
from .models import DataSource


class SparkPostDataSource(DataSource):
    data_source = models.OneToOneField(DataSource)
    host = models.CharField('Host', max_length=255)
    port = models.CharField('Port', max_length=255)
    username = models.CharField('Username', max_length=255)
    password = models.CharField('Password', max_length=255)
    database = models.CharField('Database', max_length=255)
    schema_file = models.FileField('Schema file', upload_to='file_uploads', default=None)

    class Meta:
        verbose_name = 'SparkPost Data source'
        verbose_name_plural = 'SparkPost Data sources'

    def filename(self):
        return os.path.basename(self.schema_file.name)

    def create_config_file(self):
        pass

    def update_config_file(self):
        pass

