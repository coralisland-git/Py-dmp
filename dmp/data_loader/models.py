import os
import codecs
from django.db import models
from django.contrib.auth.models import User
from customer.models import Customer
from django.conf import settings
import ruamel.yaml as yaml


class DataProvider(models.Model):
    title = models.CharField('Provider Title', max_length=255, blank=True, default="Google Analytics")
    name = models.CharField('Provider Name', max_length=255, blank=True, default="Google Analytics")
    order = models.IntegerField('Provider ordering in list', blank=True, default=999)


class DataSource(models.Model):
    user = models.ForeignKey(Customer)
    name = models.CharField('Data Source Name', max_length=255, default=None)
    data_provider = models.ForeignKey(DataProvider, null=True)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        verbose_name = 'Data source'
        verbose_name_plural = 'Data source'

    def get_configs_base_path(self):
        return os.path.join(settings.BASE_DIR, self._meta.app_label, 'embulk_configs')

    def check_provider_configs_path(self):
        path = os.path.join(self.get_configs_base_path(), 'providers', self.data_provider.name)
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def check_config_template_path(self):
        template_path = os.path.join(self.get_configs_base_path(), 'config_templates', 'template.yml')
        if os.path.exists(template_path):
            return template_path

    def get_config_template_content(self):
        template = self.check_config_template_path()
        with codecs.open(template, 'r', 'utf-8') as fi:
            template_data = yaml.round_trip_load(fi, preserve_quotes=True)
        return template_data

    def write_config_content(self, path, template_data):
        fname = os.path.join(path, "config_{user_id}_{data_source_id}.yml".format(user_id=self.user_id,
                                                                                  data_source_id=self.id))
        with codecs.open(fname, 'w', 'utf-8') as yaml_file:
            yaml_file.write(yaml.round_trip_dump(template_data, block_seq_indent=True))
        return fname

    def create_config_file(self):
        return self.write_config_content(self.check_provider_configs_path(), self.get_config_template_content())


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


class DataFlowSettings(models.Model):
    TIME_INTERVALS = ((1, '5 minutes'),
                      (2, '30 minutes'),
                      (3, '1 hour'),
                      (4, '2 hours'),
                      (5, '5 hours'),
                      (6, '10 hours'),
                      (7, '24 hours'))
    user = models.ForeignKey(Customer)
    sync_interval = models.SmallIntegerField(choices=TIME_INTERVALS, default=2)