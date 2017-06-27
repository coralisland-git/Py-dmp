from data_loader.forms import VerticaDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import VerticaDataSource


class VerticaDataSourceCreateView(DataSourceCreateView):
    details_model_class = VerticaDataSource

    def get_details_form_class(self):
        return VerticaDataSourceForm


class VerticaDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = VerticaDataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return VerticaDataSourceForm
