from data_loader.forms import OracleDBDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import OracleDBDataSource


class OracleDBDataSourceCreateView(DataSourceCreateView):
    details_model_class = OracleDBDataSource

    def get_details_form_class(self):
        return OracleDBDataSourceForm


class OracleDBDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = OracleDBDataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return OracleDBDataSourceForm
