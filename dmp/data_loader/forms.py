from django import forms
from data_loader.models import DataSource, DataFlowSettings
from django.utils.translation import ugettext_lazy as _


class DataSourceCreateForm(forms.ModelForm):

    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-input',
                                                                         'placeholder': _('Data Source Name'),
                                                                         'maxlength': 255}))

    account_id = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-input',
                                                                               'placeholder': _('Account ID'),
                                                                               'maxlength': 255}))

    upload_file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-input'}))

    class Meta:
        model = DataSource
        fields = ('name', 'account_id', 'upload_file')


class DataSourceUpdateForm(forms.Form):
    pass


class DataFlowSettingsForm(forms.ModelForm):

    sync_interval = forms.ChoiceField(choices=DataFlowSettings.TIME_INTERVALS,
                                      widget=forms.Select(attrs={'class': 'form-input dropdown'}))

    class Meta:
        model = DataFlowSettings
        fields = ('sync_interval', )
