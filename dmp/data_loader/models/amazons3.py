from django.db import models
from .models import DataSource


class AmazonS3DataSource(DataSource):
    data_source = models.OneToOneField(DataSource)
    bucket = models.CharField('S3 bucket name', max_length=255)
    path_prefix = models.CharField('Path prefix', max_length=255)
    access_key = models.CharField('Access key', max_length=255)
    secret_key = models.CharField('Secret key', max_length=255)
    endpoint = models.CharField('Endpoint URL', max_length=255)

    class Meta:
        verbose_name = 'AmazonS3 Data source'
        verbose_name_plural = 'AmazonS3 Data sources'

    def create_config_file(self):
        pass

    def update_config_file(self):
        pass

