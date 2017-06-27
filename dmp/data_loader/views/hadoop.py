from data_loader.forms import HadoopDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import HadoopDataSource


class HadoopDataSourceCreateView(DataSourceCreateView):
    details_model_class = HadoopDataSource

    def get_details_form_class(self):
        return HadoopDataSourceForm


class HadoopDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = HadoopDataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return HadoopDataSourceForm
