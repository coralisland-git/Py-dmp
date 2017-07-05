from django.conf.urls import url
from data_loader.views import *
# from data_loader.views import DataSourceListView, DataSourceCreateView, \
#     DataProviderListView, DataSourceDeleteView, DataSourceUpdateView, DataFlowSettingsUpdateView
# from data_loader.views.analytics import AnalyticsDataSourceCreateView, AnalyticsDataSourceUpdateView
# from data_loader.views.spreadsheets import SpreadsheetsDataSourceCreateView, SpreadsheetsDataSourceUpdateView
from data_loader.views.postgresql import PostgreSQLDataSourceCreateView, PostgreSQLDataSourceUpdateView
from data_loader.views.vertica import VerticaDataSourceCreateView, VerticaDataSourceUpdateView
from data_loader.views.jdbc import JDBCDataSourceCreateView, JDBCDataSourceUpdateView
from data_loader.views.mongodb import MongoDBDataSourceCreateView, MongoDBDataSourceUpdateView
from data_loader.views.ftp import FTPDataSourceCreateView, FTPDataSourceUpdateView
from data_loader.views.oracledb import OracleDBDataSourceCreateView, OracleDBDataSourceUpdateView
from data_loader.views.salesforce import SalesforceDataSourceCreateView, SalesforceDataSourceUpdateView
from data_loader.views.hadoop import HadoopDataSourceCreateView, HadoopDataSourceUpdateView
from data_loader.views.googlecloud import GoogleCloudDataSourceCreateView, GoogleCloudDataSourceUpdateView
from data_loader.views.marketo import MarketoDataSourceCreateView, MarketoDataSourceUpdateView
from data_loader.views.twitter import TwitterDataSourceCreateView, TwitterDataSourceUpdateView
from data_loader.views.dynamodb import DynamoDBDataSourceCreateView, DynamoDBDataSourceUpdateView
from data_loader.views.http import HTTPDataSourceCreateView, HTTPDataSourceUpdateView
from data_loader.views.zendesk import ZendeskDataSourceCreateView, ZendeskDataSourceUpdateView
from data_loader.views.adwords import AdwordsDataSourceCreateView, AdwordsDataSourceUpdateView

urlpatterns = [
    url(r'^$', DataSourceListView.as_view(), name='datasource-list'),

    url(r'analytics-create/(?P<provider_id>[0-9]+)/$', AnalyticsDataSourceCreateView.as_view(),
        name='analytics-datasource-create'),
    url(r'analytics-update/(?P<pk>[0-9]+)/$', AnalyticsDataSourceUpdateView.as_view(),
        name='analytics-datasource-update'),

    url(r'spreadsheets-create/(?P<provider_id>[0-9]+)/$', SpreadsheetsDataSourceCreateView.as_view(),
        name='spreadsheets-datasource-create'),
    url(r'spreadsheets-update/(?P<pk>[0-9]+)/$', SpreadsheetsDataSourceUpdateView.as_view(),
        name='spreadsheets-datasource-update'),

    url(r'postgresql-create/(?P<provider_id>[0-9]+)/$', PostgreSQLDataSourceCreateView.as_view(),
        name='postgres-datasource-create'),
    url(r'postgresql-update/(?P<pk>[0-9]+)/$', PostgreSQLDataSourceUpdateView.as_view(),
        name='postgres-datasource-update'),

    url(r'salesforce-create/(?P<provider_id>[0-9]+)/$', SalesforceDataSourceCreateView.as_view(),
        name='salesforce-datasource-create'),
    url(r'salesforce-update/(?P<pk>[0-9]+)/$', SalesforceDataSourceUpdateView.as_view(),
        name='salesforce-datasource-update'),

    url(r'amazon-create/(?P<provider_id>[0-9]+)/$', PostgreSQLDataSourceCreateView.as_view(),
        name='amazon-datasource-create'),
    url(r'amazon-update/(?P<pk>[0-9]+)/$', PostgreSQLDataSourceUpdateView.as_view(),
        name='amazon-datasource-update'),

    url(r'marketo-create/(?P<provider_id>[0-9]+)/$', MarketoDataSourceCreateView.as_view(),
        name='marketo-datasource-create'),
    url(r'marketo-update/(?P<pk>[0-9]+)/$', MarketoDataSourceUpdateView.as_view(),
        name='marketo-datasource-update'),

    url(r'mysql-create/(?P<provider_id>[0-9]+)/$', PostgreSQLDataSourceCreateView.as_view(),
        name='mysql-datasource-create'),
    url(r'mysql-update/(?P<pk>[0-9]+)/$', PostgreSQLDataSourceUpdateView.as_view(),
        name='mysql-datasource-update'),

    url(r'googlecloud-create/(?P<provider_id>[0-9]+)/$', GoogleCloudDataSourceCreateView.as_view(),
        name='googlecloud-datasource-create'),
    url(r'googlecloud-update/(?P<pk>[0-9]+)/$', GoogleCloudDataSourceUpdateView.as_view(),
        name='googlecloud-datasource-update'),

    url(r'redshift-create/(?P<provider_id>[0-9]+)/$', PostgreSQLDataSourceCreateView.as_view(),
        name='redshift-datasource-create'),
    url(r'redshift-update/(?P<pk>[0-9]+)/$', PostgreSQLDataSourceUpdateView.as_view(),
        name='redshift-datasource-update'),

    url(r'jdbc-create/(?P<provider_id>[0-9]+)/$', JDBCDataSourceCreateView.as_view(),
        name='jdbc-datasource-create'),
    url(r'jdbc-update/(?P<pk>[0-9]+)/$', JDBCDataSourceUpdateView.as_view(),
        name='jdbc-datasource-update'),

    url(r'hadoop-create/(?P<provider_id>[0-9]+)/$', HadoopDataSourceCreateView.as_view(),
        name='hadoop-datasource-create'),
    url(r'hadoop-update/(?P<pk>[0-9]+)/$', HadoopDataSourceUpdateView.as_view(),
        name='hadoop-datasource-update'),

    url(r'mixpanel-create/(?P<provider_id>[0-9]+)/$', PostgreSQLDataSourceCreateView.as_view(),
        name='mixpanel-datasource-create'),
    url(r'mixpanel-update/(?P<pk>[0-9]+)/$', PostgreSQLDataSourceUpdateView.as_view(),
        name='mixpanel-datasource-update'),

    url(r'mongodb-create/(?P<provider_id>[0-9]+)/$', MongoDBDataSourceCreateView.as_view(),
        name='mongodb-datasource-create'),
    url(r'mongodb-update/(?P<pk>[0-9]+)/$', MongoDBDataSourceUpdateView.as_view(),
        name='mongodb-datasource-update'),

    url(r'http-create/(?P<provider_id>[0-9]+)/$', HTTPDataSourceCreateView.as_view(),
        name='http-datasource-create'),
    url(r'http-update/(?P<pk>[0-9]+)/$', HTTPDataSourceUpdateView.as_view(),
        name='http-datasource-update'),

    url(r'jira-create/(?P<provider_id>[0-9]+)/$', PostgreSQLDataSourceCreateView.as_view(),
        name='jira-datasource-create'),
    url(r'jira-update/(?P<pk>[0-9]+)/$', PostgreSQLDataSourceUpdateView.as_view(),
        name='jira-datasource-update'),

    url(r'oracledb-create/(?P<provider_id>[0-9]+)/$', OracleDBDataSourceCreateView.as_view(),
        name='oracledb-datasource-create'),
    url(r'oracledb-update/(?P<pk>[0-9]+)/$', OracleDBDataSourceUpdateView.as_view(),
        name='oracledb-datasource-update'),

    url(r'zendesk-create/(?P<provider_id>[0-9]+)/$', ZendeskDataSourceCreateView.as_view(),
        name='zendesk-datasource-create'),
    url(r'zendesk-update/(?P<pk>[0-9]+)/$', ZendeskDataSourceUpdateView.as_view(),
        name='zendesk-datasource-update'),

    url(r'mssql-create/(?P<provider_id>[0-9]+)/$', PostgreSQLDataSourceCreateView.as_view(),
        name='mssql-datasource-create'),
    url(r'mssql-update/(?P<pk>[0-9]+)/$', PostgreSQLDataSourceUpdateView.as_view(),
        name='mssql-datasource-update'),

    url(r'ftp-create/(?P<provider_id>[0-9]+)/$', FTPDataSourceCreateView.as_view(),
        name='ftp-datasource-create'),
    url(r'ftp-update/(?P<pk>[0-9]+)/$', FTPDataSourceUpdateView.as_view(),
        name='ftp-datasource-update'),

    url(r'dynamodb-create/(?P<provider_id>[0-9]+)/$', DynamoDBDataSourceCreateView.as_view(),
        name='dynamodb-datasource-create'),
    url(r'dynamodb-update/(?P<pk>[0-9]+)/$', DynamoDBDataSourceUpdateView.as_view(),
        name='dynamodb-datasource-update'),

    url(r'sftp-create/(?P<provider_id>[0-9]+)/$', PostgreSQLDataSourceCreateView.as_view(),
        name='sftp-datasource-create'),
    url(r'sftp-update/(?P<pk>[0-9]+)/$', PostgreSQLDataSourceUpdateView.as_view(),
        name='sftp-datasource-update'),

    url(r'vertica-create/(?P<provider_id>[0-9]+)/$', VerticaDataSourceCreateView.as_view(),
        name='vertica-datasource-create'),
    url(r'vertica-update/(?P<pk>[0-9]+)/$', VerticaDataSourceUpdateView.as_view(),
        name='vertica-datasource-update'),

    url(r'twitter-create/(?P<provider_id>[0-9]+)/$', TwitterDataSourceCreateView.as_view(),
        name='twitter-datasource-create'),
    url(r'twitter-update/(?P<pk>[0-9]+)/$', TwitterDataSourceUpdateView.as_view(),
        name='twitter-datasource-update'),

    url(r'teradata-create/(?P<provider_id>[0-9]+)/$', PostgreSQLDataSourceCreateView.as_view(),
        name='teradata-datasource-create'),
    url(r'teradata-update/(?P<pk>[0-9]+)/$', PostgreSQLDataSourceUpdateView.as_view(),
        name='teradata-datasource-update'),

    url(r'adwords-create/(?P<provider_id>[0-9]+)/$', AdwordsDataSourceCreateView.as_view(),
        name='adwords-datasource-create'),
    url(r'adwords-update/(?P<pk>[0-9]+)/$', AdwordsDataSourceUpdateView.as_view(),
        name='adwords-datasource-update'),

    url(r'create/(?P<provider_id>[0-9]+)/$', DataSourceCreateView.as_view(), name='datasource-create'),
    url(r'update/(?P<pk>[0-9]+)/$', DataSourceUpdateView.as_view(), name='datasource-update'),
    url(r'delete/(?P<pk>[0-9]+)/$', DataSourceDeleteView.as_view(), name='datasource-delete'),
    url(r'data-providers/$', DataProviderListView.as_view(), name='datasource-providers'),
    url(r'settings/$', DataFlowSettingsUpdateView.as_view(), name='datasource-settings')
]