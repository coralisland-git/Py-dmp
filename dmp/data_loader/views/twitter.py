from data_loader.forms import TwitterDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import TwitterDataSource


class TwitterDataSourceCreateView(DataSourceCreateView):
    details_model_class = TwitterDataSource

    def get_details_form_class(self):
        return TwitterDataSourceForm


class TwitterDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = TwitterDataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return TwitterDataSourceForm
