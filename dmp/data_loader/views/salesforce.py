from data_loader.forms import SalesforceDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import SalesforceDataSource


class SalesforceDataSourceCreateView(DataSourceCreateView):
    details_model_class = SalesforceDataSource

    def get_details_form_class(self):
        return SalesforceDataSourceForm


class SalesforceDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = SalesforceDataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return SalesforceDataSourceForm
