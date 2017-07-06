import os
from django.db import models
from .models import DataSource


class AdwordsDataSource(DataSource):
    data_source = models.OneToOneField(DataSource)
    conditions = models.CharField('Query condition list', max_length=255, blank=True, null=True)
    field_list = models.CharField('Field list to query', max_length=255)
    date_range = models.CharField('Date range', max_length=255)
    report_type = models.CharField('Report type', max_length=255)
    oauth_key_file = models.FileField('OAuth2 keyfile', upload_to='file_uploads', default=None)

    class Meta:
        verbose_name = 'Adwords Data source'
        verbose_name_plural = 'Adwords Data sources'

    def filename(self):
        return os.path.basename(self.oauth_key_file.name)

    def create_config_file(self):
        pass

    def update_config_file(self):
        pass

