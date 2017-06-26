from data_loader.forms import JDBCDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import JDBCDataSource


class JDBCDataSourceCreateView(DataSourceCreateView):
    details_model_class = JDBCDataSource

    def get_details_form_class(self):
        return JDBCDataSourceForm


class JDBCDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = JDBCDataSource

    def get_detailed_data_source_object(self):
        # AnalyticsDataSource.objects.get(data_source=self.object)
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return JDBCDataSourceForm
