from data_loader.forms import MixpanelDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import MixpanelDataSource


class MixpanelDataSourceCreateView(DataSourceCreateView):
    details_model_class = MixpanelDataSource

    def get_details_form_class(self):
        return MixpanelDataSourceForm


class MixpanelDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = MixpanelDataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return MixpanelDataSourceForm
