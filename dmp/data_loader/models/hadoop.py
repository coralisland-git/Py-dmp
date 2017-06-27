import os
from django.db import models
from .models import DataSource


class HadoopDataSource(DataSource):
    data_source = models.OneToOneField(DataSource)
    path = models.CharField('File path on OS', max_length=255)
    os_config_file = models.FileField('OS config file', upload_to='file_uploads', default=None)
    os_config_params = models.CharField('Config file parameters', max_length=255)
    log_level = models.CharField('Logging level', max_length=255)

    class Meta:
        verbose_name = 'Hadoop Data source'
        verbose_name_plural = 'Hadoop Data sources'

    def filename(self):
        return os.path.basename(self.os_config_file.name)

    def create_config_file(self):
        pass

    def update_config_file(self):
        pass

