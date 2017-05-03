from django.db import models
from django.contrib.auth.models import User
from customer.models import Customer


class DataSource(models.Model):

    user = models.ForeignKey(Customer)
    title = models.CharField('Title', max_length=255)
    data_source = models.CharField('Data source', max_length=255, blank=True, default=None)
    provider = models.CharField('Data source', max_length=255, blank=True, default="Google Analytics")
    account_id = models.CharField('Account ID', max_length=255, blank=True, default=None)
    upload_file = models.FileField('Upload file', upload_to='ga_uploads', blank=True, default=None)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        verbose_name = 'Data source'
        verbose_name_plural = 'Data source'

