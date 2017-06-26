from data_loader.forms import MongoDBDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import MongoDBDataSource


class MongoDBDataSourceCreateView(DataSourceCreateView):
    details_model_class = MongoDBDataSource

    def get_details_form_class(self):
        return MongoDBDataSourceForm


class MongoDBDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = MongoDBDataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return MongoDBDataSourceForm
