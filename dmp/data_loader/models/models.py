import os
import codecs
from django.db import models
from customer.models import Customer
from django.conf import settings
import ruamel.yaml as yaml


class DataProvider(models.Model):
    title = models.CharField('Provider Title', max_length=255, blank=True, default="Google Analytics")
    name = models.CharField('Provider Name', max_length=255, blank=True, default="Google Analytics")
    order = models.IntegerField('Provider ordering in list', blank=True, default=999)

    def get_add_url_name(self):
        return 'data_loader:{}-datasource-create'.format(self.name)


class DataSource(models.Model):
    user = models.ForeignKey(Customer)
    name = models.CharField('Data Source Name', max_length=255, default=None)
    data_provider = models.ForeignKey(DataProvider, null=True)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        verbose_name = 'Data source'
        verbose_name_plural = 'Data source'

    def get_update_url_name(self):
        return 'data_loader:{}-datasource-update'.format(self.data_provider.name)

    def get_output_table_name(self):
        return "Default table name for output storage - {provider_name}_{user_id}_{data_source_id}"\
            .format(provider_name=self.data_provider.name,
                    user_id=self.user.id,
                    data_source_id=self.id)

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

    def get_config_template_content(self, path=None):
        if path:
            try:
                with codecs.open(path, 'r', 'utf-8') as fi:
                    config_data = yaml.round_trip_load(fi, preserve_quotes=True)
            except FileNotFoundError:
                template = self.check_config_template_path()
                with codecs.open(template, 'r', 'utf-8') as fi:
                    config_data = yaml.round_trip_load(fi, preserve_quotes=True)
            return config_data
        else:
            template = self.check_config_template_path()
            with codecs.open(template, 'r', 'utf-8') as fi:
                template_data = yaml.round_trip_load(fi, preserve_quotes=True)
            return template_data

    def write_config_content(self, path, template_data):
        fname = os.path.join(path, "config_{user_id}_{data_source_id}.yml".format(user_id=self.user.id,
                                                                                  data_source_id=self.id))
        with codecs.open(fname, 'w', 'utf-8') as yaml_file:
            yaml_file.write(yaml.round_trip_dump(template_data, block_seq_indent=True))
        return fname

    def create_config_file(self):
        return self.write_config_content(self.check_provider_configs_path(), self.get_config_template_content())


class DataFlowSettings(models.Model):
    TIME_INTERVALS = ((2, '30 minutes'),
                      (3, '1 hour'),
                      (4, '2 hours'),
                      (5, '5 hours'),
                      (6, '10 hours'),
                      (7, '24 hours'))
    user = models.ForeignKey(Customer)
    sync_interval = models.SmallIntegerField(choices=TIME_INTERVALS, default=2)
