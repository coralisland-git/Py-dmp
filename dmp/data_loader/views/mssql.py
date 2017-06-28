from data_loader.forms import MSSQLDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import MSSQLDataSource


class MSSQLDataSourceCreateView(DataSourceCreateView):
    details_model_class = MSSQLDataSource

    def get_details_form_class(self):
        return MSSQLDataSourceForm


class MSSQLDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = MSSQLDataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return MSSQLDataSourceForm
