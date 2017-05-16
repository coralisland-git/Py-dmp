import os
from django.db import models
from django.contrib.auth.models import User
from customer.models import Customer
from django.conf import settings


class DataProvider(models.Model):
    title = models.CharField('Provider Title', max_length=255, blank=True, default="Google Analytics")
    name = models.CharField('Provider Name', max_length=255, blank=True, default="Google Analytics")
    order = models.IntegerField('Provider ordering in list', blank=True, default=999)


class DataSource(models.Model):
    user = models.ForeignKey(Customer)
    name = models.CharField('Data Source Name', max_length=255, default=None)
    data_provider = models.ForeignKey(DataProvider, null=True)
    account_id = models.CharField('Account ID', max_length=255, blank=True, default=None)
    upload_file = models.FileField('Upload file', upload_to='file_uploads', blank=True, default=None)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        verbose_name = 'Data source'
        verbose_name_plural = 'Data source'

    def filename(self):
        return os.path.basename(self.upload_file.name)

    def check_config_path(self):
        path = os.path.join(settings.BASE_DIR, self._meta.app_label, 'embulk_configs', self.data_provider.name)
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    #TODO: debug and adjust configs after redshift and superset full setup
    # def create_config_file(self, path):
    #
    #     import yaml
    #
    #     fname = os.path.join(path, "config.yml")
    #
    #     stream = open(fname, 'r')
    #     data = yaml.load(stream)
    #
    #     data['instances'][0]['host'] = '1.2.3.4'
    #     data['instances'][0]['username'] = 'Username'
    #     data['instances'][0]['password'] = 'Password'
    #
    #     with open(fname, 'w') as yaml_file:
    #         yaml_file.write(yaml.dump(data, default_flow_style=False))
    #
    # def generate_config(self):
    #     self.create_config_file(self.check_config_path())

class DataFlowSettings(models.Model):
    TIME_INTERVALS = ((1, '30 minutes'),
                      (2, '1 hour'),
                      (3, '2 hours'),
                      (4, '5 hours'),
                      (5, '10 hours'),
                      (6, '24 hours'))
    user = models.ForeignKey(Customer)
    sync_interval = models.SmallIntegerField(choices=TIME_INTERVALS, default=1)