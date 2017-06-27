from data_loader.forms import GoogleCloudDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import GoogleCloudDataSource


class GoogleCloudDataSourceCreateView(DataSourceCreateView):
    details_model_class = GoogleCloudDataSource

    def get_details_form_class(self):
        return GoogleCloudDataSourceForm


class GoogleCloudDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = GoogleCloudDataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return GoogleCloudDataSourceForm
