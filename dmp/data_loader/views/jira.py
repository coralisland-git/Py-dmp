from data_loader.forms import JiraDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import JiraDataSource


class JiraDataSourceCreateView(DataSourceCreateView):
    details_model_class = JiraDataSource

    def get_details_form_class(self):
        return JiraDataSourceForm


class JiraDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = JiraDataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return JiraDataSourceForm
