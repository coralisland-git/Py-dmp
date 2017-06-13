from django.conf.urls import url

from data_loader.views import DataSourceListView, DataSourceCreateView, \
    DataProviderListView, DataSourceDeleteView, DataSourceUpdateView, DataFlowSettingsUpdateView
from data_loader.views.analytics import AnalyticsDataSourceCreateView, AnalyticsDataSourceUpdateView
from data_loader.views.spreadsheets import SpreadsheetsDataSourceCreateView, SpreadsheetsDataSourceUpdateView

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
    url(r'create/(?P<provider_id>[0-9]+)/$', DataSourceCreateView.as_view(), name='datasource-create'),
    url(r'update/(?P<pk>[0-9]+)/$', DataSourceUpdateView.as_view(), name='datasource-update'),
    url(r'delete/(?P<pk>[0-9]+)/$', DataSourceDeleteView.as_view(), name='datasource-delete'),
    url(r'data-providers/$', DataProviderListView.as_view(), name='datasource-providers'),
    url(r'settings/$', DataFlowSettingsUpdateView.as_view(), name='datasource-settings')
]