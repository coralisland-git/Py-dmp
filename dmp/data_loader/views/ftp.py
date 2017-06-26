from data_loader.forms import FTPDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import FTPDataSource


class FTPDataSourceCreateView(DataSourceCreateView):
    details_model_class = FTPDataSource

    def get_details_form_class(self):
        return FTPDataSourceForm


class FTPDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = FTPDataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return FTPDataSourceForm
