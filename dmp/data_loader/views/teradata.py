from data_loader.forms import TeradataDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import TeradataDataSource


class TeradataDataSourceCreateView(DataSourceCreateView):
    details_model_class = TeradataDataSource

    def get_details_form_class(self):
        return TeradataDataSourceForm


class TeradataDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = TeradataDataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return TeradataDataSourceForm
