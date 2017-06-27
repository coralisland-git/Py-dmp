from data_loader.forms import MarketoDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import MarketoDataSource


class MarketoDataSourceCreateView(DataSourceCreateView):
    details_model_class = MarketoDataSource

    def get_details_form_class(self):
        return MarketoDataSourceForm


class MarketoDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = MarketoDataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return MarketoDataSourceForm
