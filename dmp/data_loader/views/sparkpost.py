from data_loader.forms import SparkPostDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import SparkPostDataSource


class SparkPostDataSourceCreateView(DataSourceCreateView):
    details_model_class = SparkPostDataSource

    def get_details_form_class(self):
        return SparkPostDataSourceForm


class SparkPostDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = SparkPostDataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return SparkPostDataSourceForm
