import os
from django.db import models
from .models import DataSource


class TwitterDataSource(DataSource):
    data_source = models.OneToOneField(DataSource)
    account_id = models.CharField('Twitter user ID', max_length=255)
    archive_id = models.CharField('Archive/Feed ID', max_length=255)
    archive_link = models.CharField('Archive/Feed Public Link', max_length=255)

    class Meta:
        verbose_name = 'Twitter Data source'
        verbose_name_plural = 'Twitter Data sources'

    def create_config_file(self):
        pass

    def update_config_file(self):
        pass

