from django.db import models
from django.contrib.auth.models import User


class DataSource(models.Model):

    user = models.ForeignKey(User)
    title = models.CharField('Title', max_length=255)
    data_source = models.CharField('Data source', max_length=255)
    account_id = models.CharField('Account ID', max_length=255)
    upload_file = models.FileField('Upload file', upload_to='ga_uploads', blank=True, default=None)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        verbose_name = 'Data source'
        verbose_name_plural = 'Data source'

