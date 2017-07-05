from data_loader.forms import RedshiftDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import RedshiftDataSource


class RedshiftDataSourceCreateView(DataSourceCreateView):
    details_model_class = RedshiftDataSource

    def get_details_form_class(self):
        return RedshiftDataSourceForm


class RedshiftDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = RedshiftDataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return RedshiftDataSourceForm
