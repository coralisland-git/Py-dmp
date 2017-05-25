from django import forms
from data_loader.models import DataSource, DataFlowSettings
from django.utils.translation import ugettext_lazy as _
from django.core.validators import FileExtensionValidator


class DataSourceCreateForm(forms.ModelForm):

    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-input',
                                                                         'placeholder': _('Data Source Name'),
                                                                         'maxlength': 255}))

    account_id = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={'class': 'form-input',
                                                                               'placeholder': _('ID'),
                                                                               'maxlength': 255}))

    upload_file = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-input'}),
                                  validators=[FileExtensionValidator(allowed_extensions=['json'])])

    # google-spreadsheets specific field
    document_url = forms.CharField(max_length=355, required=False, widget=forms.TextInput(attrs={'class': 'form-input',
                                                                               'placeholder': _('Spreadsheets URL'),
                                                                               'maxlength': 355}))

    class Meta:
        model = DataSource
        fields = ('name', 'account_id', 'upload_file', 'document_url')


class DataSourceUpdateForm(forms.Form):
    pass


class DataFlowSettingsForm(forms.ModelForm):

    sync_interval = forms.ChoiceField(choices=DataFlowSettings.TIME_INTERVALS,
                                      widget=forms.Select(attrs={'class': 'form-input dropdown'}))

    class Meta:
        model = DataFlowSettings
        fields = ('sync_interval', )
