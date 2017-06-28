from django.db import models
from .models import DataSource


class MixpanelDataSource(DataSource):
    data_source = models.OneToOneField(DataSource)
    key = models.CharField('Project API Key', max_length=255)
    secret = models.CharField('Project API Secret', max_length=255)
    timezone = models.CharField('Project timezone', max_length=255)

    class Meta:
        verbose_name = 'Mixpanel Data source'
        verbose_name_plural = 'Mixpanel Data sources'

    def create_config_file(self):
        pass

    def update_config_file(self):
        pass

