from data_loader.forms import MySQLDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import MySQLDataSource


class MySQLDataSourceCreateView(DataSourceCreateView):
    details_model_class = MySQLDataSource

    def get_details_form_class(self):
        return MySQLDataSourceForm


class MySQLDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = MySQLDataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return MySQLDataSourceForm
