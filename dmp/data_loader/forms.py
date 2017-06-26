from django import forms
from data_loader.models import DataSource, DataFlowSettings, AnalyticsDataSource, SpreadsheetsDataSource, \
    PostgreSQLDataSource, VerticaDataSource, JDBCDataSource
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

    upload_file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-input'}),
                                  validators=[FileExtensionValidator(allowed_extensions=['json'])])

    dimensions = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Analytics dimensions'),
               'maxlength': 255}))

    metrics = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Analytics metrics'),
               'maxlength': 255}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(AnalyticsDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = AnalyticsDataSource
        fields = ('account_id', 'upload_file', 'dimensions', 'metrics')


class SpreadsheetsDataSourceForm(forms.ModelForm):

    worksheet_id = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('ID'),
               'maxlength': 255}))

    upload_file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-input'}),
                                  validators=[FileExtensionValidator(allowed_extensions=['json'])])

    document_url = forms.CharField(max_length=355, widget=forms.TextInput(attrs={'class': 'form-input',
                                                                                 'placeholder': _('Spreadsheets URL'),
                                                                                 'maxlength': 355}))

    field_type0 = forms.ChoiceField(choices=list((x,y) for x,y  in enumerate(SpreadsheetsDataSource.COLUMN_TYPES)),
                                    widget=forms.Select(attrs={'class': 'form-input'})
                                    )

    field_name0 = forms.CharField(max_length=100, error_messages={'required': 'Please, provide information '
                                                                              'about one field at least.'},
                                  widget=forms.TextInput(attrs={'class': 'form-input',
                                                                'placeholder': _('Field name'),
                                                                'maxlength': 100}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(SpreadsheetsDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = SpreadsheetsDataSource
        fields = ('worksheet_id', 'upload_file', 'document_url')

    def prepare_fields_list(self):
        fields_count = 0
        fields = list()
        for key in self.request.POST.keys():
            if 'field_name' in key:
                fields_count += 1

        for i in range(0, fields_count):
            fields.append({"order": i,
                           "name": self.request.POST.get('field_name'+str(i)),
                           "type": SpreadsheetsDataSource.COLUMN_TYPES[int(self.request.POST.get('field_type'+str(i)))]})
        return fields

    def save(self, commit=True):
        spreadsheets_ds = super(SpreadsheetsDataSourceForm, self).save(commit=False)
        spreadsheets_ds.field_list = self.prepare_fields_list()

        if commit:
            spreadsheets_ds.save()
        return spreadsheets_ds


class DataSourceUpdateForm(forms.Form):
    pass


class DataFlowSettingsForm(forms.ModelForm):

    sync_interval = forms.ChoiceField(choices=DataFlowSettings.TIME_INTERVALS,
                                      widget=forms.Select(attrs={'class': 'form-input dropdown'}))

    class Meta:
        model = DataFlowSettings
        fields = ('sync_interval', )


class PostgreSQLDataSourceForm(forms.ModelForm):

    host = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Host name'),
               'maxlength': 255}))

    port = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Port number'),
               'maxlength': 255}))

    username = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Username'),
               'maxlength': 255}))

    password = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Password'),
               'maxlength': 255}))

    database = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Database name'),
               'maxlength': 255}))

    schema_file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-input'}),
                                  validators=[FileExtensionValidator(allowed_extensions=['json', 'yaml'])])

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(PostgreSQLDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PostgreSQLDataSource
        fields = ('host', 'port', 'username', 'password', 'database', 'schema_file')


class VerticaDataSourceForm(forms.ModelForm):

    host = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Host name'),
               'maxlength': 255}))

    port = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Port number'),
               'maxlength': 255}))

    username = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Username'),
               'maxlength': 255}))

    password = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Password'),
               'maxlength': 255}))

    database = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Database name'),
               'maxlength': 255}))

    schema_name = forms.CharField(max_length=255,
                             widget=forms.TextInput(attrs={'class': 'form-input',
                                                                    'placeholder': _('Destination schema name'),
                                                                    'maxlength': 255}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(VerticaDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = VerticaDataSource
        fields = ('host', 'port', 'username', 'password', 'database', 'schema_name', )


class JDBCDataSourceForm(forms.ModelForm):

    url = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('URL of the JDBC connection (e.g. "jdbc:sqlite:mydb.sqlite3")'),
               'maxlength': 255}))

    driver_class = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Class name of the JDBC driver (e.g. "org.sqlite.JDBC")'),
               'maxlength': 255}))

    username = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Username'),
               'maxlength': 255}))

    password = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Password'),
               'maxlength': 255}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(JDBCDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = JDBCDataSource
        fields = ('url', 'driver_class', 'username', 'password')