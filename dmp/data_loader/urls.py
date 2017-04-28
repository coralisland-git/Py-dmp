from django.conf.urls import url

from data_loader.views import DataSourceListView

urlpatterns = [
    url(r'^$', DataSourceListView.as_view(), name='datasources-list'),
]