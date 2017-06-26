from data_loader.forms import PostgreSQLDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import PostgreSQLDataSource


class PostgreSQLDataSourceCreateView(DataSourceCreateView):
    details_model_class = PostgreSQLDataSource

    def get_details_form_class(self):
        return PostgreSQLDataSourceForm


class PostgreSQLDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = PostgreSQLDataSource

    def get_detailed_data_source_object(self):
        # AnalyticsDataSource.objects.get(data_source=self.object)
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return PostgreSQLDataSourceForm
