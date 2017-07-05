from django.db import models
from .models import DataSource


class JiraDataSource(DataSource):
    data_source = models.OneToOneField(DataSource)
    uri = models.CharField('JIRA API endpoint', max_length=255)
    username = models.CharField('Username', max_length=255)
    password = models.CharField('Password', max_length=255)
    jql = models.CharField('JQL', max_length=255)
    issue_columns = models.CharField('Issue attributes', max_length=255)

    class Meta:
        verbose_name = 'Jira Data source'
        verbose_name_plural = 'Jira Data sources'

    def create_config_file(self):
        pass

    def update_config_file(self):
        pass

