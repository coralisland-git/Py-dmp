from data_loader.forms import SFTPDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import SFTPDataSource


class SFTPDataSourceCreateView(DataSourceCreateView):
    details_model_class = SFTPDataSource

    def get_details_form_class(self):
        return SFTPDataSourceForm


class SFTPDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = SFTPDataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return SFTPDataSourceForm
