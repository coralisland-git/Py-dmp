import os
from django.db import models
from .models import DataSource


class SFTPDataSource(DataSource):
    data_source = models.OneToOneField(DataSource)
    host = models.CharField('Host', max_length=255)
    port = models.CharField('Port', max_length=255)
    username = models.CharField('Username', max_length=255)
    password = models.CharField('Password', max_length=255)
    prefix = models.CharField('Path prefix', max_length=255)
    passphrase = models.CharField('Passphrase', max_length=255)
    secret_key = models.FileField('Secret key file', upload_to='file_uploads', default=None)

    class Meta:
        verbose_name = 'SFTP Data source'
        verbose_name_plural = 'SFTP Data sources'

    def filename(self):
        return os.path.basename(self.secret_key.name)

    def create_config_file(self):
        pass

    def update_config_file(self):
        pass

