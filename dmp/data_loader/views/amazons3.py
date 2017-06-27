from data_loader.forms import AmazonS3DataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import AmazonS3DataSource


class AmazonS3DataSourceCreateView(DataSourceCreateView):
    details_model_class = AmazonS3DataSource

    def get_details_form_class(self):
        return AmazonS3DataSourceForm


class AmazonS3DataSourceUpdateView(DataSourceUpdateView):
    details_model_class = AmazonS3DataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return AmazonS3DataSourceForm
