import os
from django.db import models
from .models import DataSource


class HTTPDataSource(DataSource):
    data_source = models.OneToOneField(DataSource)
    url = models.CharField('Base URL', max_length=255)
    method = models.CharField('HTTP method', max_length=255)
    params = models.CharField('Query params', max_length=255)

    class Meta:
        verbose_name = 'HTTP Data source'
        verbose_name_plural = 'HTTP Data sources'

    def create_config_file(self):
        pass

    def update_config_file(self):
        pass

