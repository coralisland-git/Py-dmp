import os
from django.db import models
from django.contrib.auth.models import User
from customer.models import Customer


class DataSource(models.Model):

    user = models.ForeignKey(Customer)
    name = models.CharField('Data Source Name', max_length=255, default=None)
    provider = models.CharField('Provider', max_length=255, blank=True, default="Google Analytics")
    account_id = models.CharField('Account ID', max_length=255, blank=True, default=None)
    upload_file = models.FileField('Upload file', upload_to='file_uploads', blank=True, default=None)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        verbose_name = 'Data source'
        verbose_name_plural = 'Data source'

    def filename(self):
        return os.path.basename(self.upload_file.name)

