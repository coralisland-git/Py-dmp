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
    account_id = models.CharField('Account ID', max_length=255, default=None)
    upload_file = models.FileField('Upload file', upload_to='file_uploads', default=None)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        verbose_name = 'Data source'
        verbose_name_plural = 'Data source'

    def filename(self):
        return os.path.basename(self.upload_file.name)

    def base_path(self):
        return os.path.join(settings.BASE_DIR, self._meta.app_label, 'embulk_configs')

    def check_config_path(self):
        path = os.path.join(self.base_path(), 'providers', self.data_provider.name)
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def check_config_template(self):
        template_path = os.path.join(self.base_path(), 'config_templates', 'template.yml')
        if os.path.exists(template_path):
            return template_path

    def create_config_file(self, path):
        from django.conf import settings
        template = self.check_config_template()
        if template:
            with codecs.open(template, 'r', 'utf-8') as fi:
                template_data = yaml.round_trip_load(fi, preserve_quotes=True)
            with codecs.open(os.path.join(settings.MEDIA_ROOT, self.upload_file.name), 'r', 'utf-8') as key_file:
                key_data = key_file.read()
            template_data['in']['json_key_content'] = key_data
            template_data['in']['view_id'] = self.account_id
            template_data['out']['table'] = "{}_{}".format(self.data_provider.name, self.account_id)

            fname = os.path.join(path, "config_{}.yml".format(self.account_id))
            with codecs.open(fname, 'w', 'utf-8') as yaml_file:
                yaml_file.write(yaml.round_trip_dump(template_data, block_seq_indent=True))
            return fname

    def generate_config(self):
        return self.create_config_file(self.check_config_path())

    def process_data(self, fname):
        from subprocess import call
        log_path = os.path.join(settings.BASE_DIR, 'logs')
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        log_file = open(os.path.join(log_path, 'embulk_stdout.log'), "w+")
        # call("which embulk; embulk".format(embulk_path=settings.EMBULK_USER_PATH), shell=True, stdout=log_file)
        return call("w; whoami; . {embulk_path}.bashrc; {embulk_path}.embulk/bin/embulk gem list".format(embulk_path=settings.EMBULK_USER_PATH,
                                                                            filename=fname), shell=True, stdout=log_file)


class DataFlowSettings(models.Model):
    TIME_INTERVALS = ((1, '30 minutes'),
                      (2, '1 hour'),
                      (3, '2 hours'),
                      (4, '5 hours'),
                      (5, '10 hours'),
                      (6, '24 hours'))
    user = models.ForeignKey(Customer)
    sync_interval = models.SmallIntegerField(choices=TIME_INTERVALS, default=1)