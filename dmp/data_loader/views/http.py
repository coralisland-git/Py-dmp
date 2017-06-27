from data_loader.forms import HTTPDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import HTTPDataSource


class HTTPDataSourceCreateView(DataSourceCreateView):
    details_model_class = HTTPDataSource

    def get_details_form_class(self):
        return HTTPDataSourceForm


class HTTPDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = HTTPDataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return HTTPDataSourceForm
