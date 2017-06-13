import os
import codecs
from django.db import models
from .models import DataSource
import ruamel.yaml as yaml


class SpreadsheetsDataSource(DataSource):
    data_source = models.OneToOneField(DataSource)
    worksheet_id = models.CharField('Account ID', max_length=255, default=None)
    upload_file = models.FileField('Upload file', upload_to='file_uploads', default=None)
    document_url = models.CharField('Document URL', max_length=355, default=None)

    class Meta:
        verbose_name = 'Google Analytics Data source'
        verbose_name_plural = 'Google Analytics Data source'

    #TODO: Refactor all things which not related on details model but on linked DataSource model
    # (check_config_template_path, check_provider_configs_path, update_config_content_for_analytics, write_config_content)

    def filename(self):
        return os.path.basename(self.upload_file.name)

    def check_config_template_path(self):
        template_path = os.path.join(self.get_configs_base_path(), 'config_templates', 'spreadsheets_template.yml')
        if os.path.exists(template_path):
            return template_path

    def write_config_content(self, path, template_data):
        fname = os.path.join(path, "config_{user_id}_{data_source_id}.yml".format(user_id=self.data_source.user_id,
                                                                                  data_source_id=self.id))
        with codecs.open(fname, 'w', 'utf-8') as yaml_file:
            yaml_file.write(yaml.round_trip_dump(template_data, block_seq_indent=True))
        return fname

    def check_provider_configs_path(self):
        path = os.path.join(self.get_configs_base_path(), 'providers', self.data_source.data_provider.name)
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def update_config_content_for_analytics(self, template_data):
        from django.conf import settings
        with codecs.open(os.path.join(settings.MEDIA_ROOT, self.upload_file.name), 'r', 'utf-8') as key_file:
            key_data = key_file.read()
        template_data['in']['json_keyfile'] = key_data
        template_data['in']['spreadsheets_url'] = self.document_url
        template_data['in']['worksheet_title'] = self.worksheet_id
        template_data['out']['table'] = "{}_{}_{}".format(self.data_source.data_provider.name,
                                                          self.data_source.user_id,
                                                          self.id)
        return template_data

    def create_config_file(self):
        template_content = self.get_config_template_content()
        template_content = self.update_config_content_for_analytics(template_content)
        return self.write_config_content(self.check_provider_configs_path(), template_content)