from data_loader.forms import AnalyticsDataSourceForm
from data_loader.views import DataSourceCreateView


class AnalyticsDataSourceCreateView(DataSourceCreateView):

    def get_details_form_class(self):
        return AnalyticsDataSourceForm
