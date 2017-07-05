from data_loader.forms import AdwordsDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import AdwordsDataSource


class AdwordsDataSourceCreateView(DataSourceCreateView):

    def get_details_form_class(self):
        return AdwordsDataSourceForm


class AdwordsDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = AdwordsDataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return AdwordsDataSourceForm
