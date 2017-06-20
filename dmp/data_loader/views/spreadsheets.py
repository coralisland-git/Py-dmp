from data_loader.forms import SpreadsheetsDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import SpreadsheetsDataSource


class SpreadsheetsDataSourceCreateView(DataSourceCreateView):
    details_model_class = SpreadsheetsDataSource

    def get_details_form_class(self):
        return SpreadsheetsDataSourceForm


class SpreadsheetsDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = SpreadsheetsDataSource

    def get_detailed_data_source_object(self):
        # AnalyticsDataSource.objects.get(data_source=self.object)
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return SpreadsheetsDataSourceForm
