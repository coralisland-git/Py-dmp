from django import forms
from data_loader.models import DataSource, DataFlowSettings, AnalyticsDataSource, SpreadsheetsDataSource
from django.utils.translation import ugettext_lazy as _
from django.core.validators import FileExtensionValidator


class DataSourceCreateForm(forms.ModelForm):

    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-input',
                                                                         'placeholder': _('Data Source Name'),
                                                                         'maxlength': 255}))

    class Meta:
        model = DataSource
        fields = ('name',)


class AnalyticsDataSourceForm(forms.ModelForm):
    account_id = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('ID'),
               'maxlength': 255}))

    upload_file = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-input'}),
                                  validators=[FileExtensionValidator(allowed_extensions=['json'])])

    dimensions = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Analytics dimensions'),
               'maxlength': 255}))

    metrics = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Analytics metrics'),
               'maxlength': 255}))

    class Meta:
        model = AnalyticsDataSource
        fields = ('account_id', 'upload_file', 'dimensions', 'metrics')


class SpreadsheetsDataSourceForm(forms.ModelForm):

    worksheet_id = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('ID'),
               'maxlength': 255}))

    upload_file = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-input'}),
                                  validators=[FileExtensionValidator(allowed_extensions=['json'])])

    document_url = forms.CharField(max_length=355, widget=forms.TextInput(attrs={'class': 'form-input',
                                                                                 'placeholder': _('Spreadsheets URL'),
                                                                                 'maxlength': 355}))

    class Meta:
        model = SpreadsheetsDataSource
        fields = ('worksheet_id', 'upload_file', 'document_url')


class DataSourceUpdateForm(forms.Form):
    pass


class DataFlowSettingsForm(forms.ModelForm):

    sync_interval = forms.ChoiceField(choices=DataFlowSettings.TIME_INTERVALS,
                                      widget=forms.Select(attrs={'class': 'form-input dropdown'}))

    class Meta:
        model = DataFlowSettings
        fields = ('sync_interval', )


Provider_DataSources_Forms_Set = {
    'analytics': AnalyticsDataSourceForm
}