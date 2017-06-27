import os
from django.db import models
from .models import DataSource


class MarketoDataSource(DataSource):
    data_source = models.OneToOneField(DataSource)
    endpoint = models.CharField('SOAP endpoint URL', max_length=255)
    account_id = models.FileField('User ID', upload_to='file_uploads', default=None)
    key_file = models.FileField('Encryption key', upload_to='file_uploads', default=None)
    start_time = models.CharField('Fetch leads start time', max_length=255)

    class Meta:
        verbose_name = 'Marketo Data source'
        verbose_name_plural = 'Marketo Data sources'

    def filename(self):
        return os.path.basename(self.key_file.name)

    def create_config_file(self):
        pass

    def update_config_file(self):
        pass

