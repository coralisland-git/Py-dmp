from data_loader.forms import ZendeskDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import ZendeskDataSource


class ZendeskDataSourceCreateView(DataSourceCreateView):
    details_model_class = ZendeskDataSource

    def get_details_form_class(self):
        return ZendeskDataSourceForm


class ZendeskDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = ZendeskDataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return ZendeskDataSourceForm
