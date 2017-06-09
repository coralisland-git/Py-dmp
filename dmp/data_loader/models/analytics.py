import os
import codecs
from django.db import models
from .models import DataSource


class AnalyticsDataSource(DataSource):
    data_source = models.OneToOneField(DataSource)
    account_id = models.CharField('Account ID', max_length=255, default=None)
    upload_file = models.FileField('Upload file', upload_to='file_uploads', default=None)
    # document_url = models.CharField('Document URL', max_length=355, default=None, blank=True, null=True)
    dimensions = models.CharField('Analytics dimensions', max_length=355, blank=True, null=True)
    metrics = models.CharField('Analytics metrics', max_length=355, blank=True, null=True)

    class Meta:
        verbose_name = 'Google Analytics Data source'
        verbose_name_plural = 'Google Analytics Data source'

    def filename(self):
        return os.path.basename(self.upload_file.name)

    def update_config_content_for_analytics(self, template_data):
        from django.conf import settings
        with codecs.open(os.path.join(settings.MEDIA_ROOT, self.upload_file.name), 'r', 'utf-8') as key_file:
            key_data = key_file.read()
        template_data['in']['json_key_content'] = key_data
        template_data['in']['view_id'] = self.account_id
        template_data['out']['table'] = "{}_{}".format(self.data_provider.name, self.account_id)
        return template_data

    def create_config_file(self):
        template_content = self.get_config_template_content()
        template_content = self.update_config_content_for_analytics(template_content)
        return self.write_config_content(self.check_provider_configs_path(), template_content)