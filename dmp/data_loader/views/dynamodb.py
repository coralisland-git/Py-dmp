from data_loader.forms import DynamoDBDataSourceForm
from data_loader.views import DataSourceCreateView, DataSourceUpdateView
from data_loader.models import DynamoDBDataSource


class DynamoDBDataSourceCreateView(DataSourceCreateView):
    details_model_class = DynamoDBDataSource

    def get_details_form_class(self):
        return DynamoDBDataSourceForm


class DynamoDBDataSourceUpdateView(DataSourceUpdateView):
    details_model_class = DynamoDBDataSource

    def get_detailed_data_source_object(self):
        return self.details_model_class.objects.get(data_source=self.object)

    def get_details_form_class(self):
        return DynamoDBDataSourceForm
