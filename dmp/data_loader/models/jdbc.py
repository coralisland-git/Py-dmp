from django.db import models
from .models import DataSource


class JDBCDataSource(DataSource):
    data_source = models.OneToOneField(DataSource)
    url = models.CharField('Host', max_length=255)
    driver_class = models.CharField('Port', max_length=255)
    username = models.CharField('Username', max_length=255)
    password = models.CharField('Password', max_length=255)

    class Meta:
        verbose_name = 'JDBC Data source'
        verbose_name_plural = 'JDBC Data sources'

    def create_config_file(self):
        pass

    def update_config_file(self):
        pass

