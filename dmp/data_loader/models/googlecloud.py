import os
from django.db import models
from .models import DataSource


class GoogleCloudDataSource(DataSource):
    data_source = models.OneToOneField(DataSource)
    bucket = models.CharField('Bucket', max_length=255)
    paths = models.CharField('Paths', max_length=255)
    account_email = models.CharField('Account email', max_length=255)
    private_key = models.FileField('Private key', upload_to='file_uploads', default=None)
    app_name = models.CharField('Application name', max_length=255)

    class Meta:
        verbose_name = 'GoogleCloud Data source'
        verbose_name_plural = 'GoogleCloud Data sources'

    def filename(self):
        return os.path.basename(self.private_key.name)

    def create_config_file(self):
        pass

    def update_config_file(self):
        pass

