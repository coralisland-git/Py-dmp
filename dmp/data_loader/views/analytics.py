from data_loader.forms import AnalyticsDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import AnalyticsDataSource


class AnalyticsDataSourceCreateView(DataSourceCreateView):

    def get_details_form_class(self):
        return AnalyticsDataSourceForm


class AnalyticsDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = AnalyticsDataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return AnalyticsDataSourceForm
