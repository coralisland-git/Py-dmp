import os
from django.db import models
from .models import DataSource


class SparkPostDataSource(DataSource):
    data_source = models.OneToOneField(DataSource)
    url = models.CharField('URL endpoint', max_length=500)
    api_key = models.CharField('Auth API key', max_length=500)

    class Meta:
        verbose_name = 'SparkPost Data source'
        verbose_name_plural = 'SparkPost Data sources'

    def create_config_file(self):
        pass

    def update_config_file(self):
        pass

