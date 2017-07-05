from django import forms
from data_loader.models import DataSource, DataFlowSettings, AnalyticsDataSource, SpreadsheetsDataSource, \
    PostgreSQLDataSource, VerticaDataSource, JDBCDataSource, OracleDBDataSource, MongoDBDataSource, FTPDataSource, \
    SalesforceDataSource, HadoopDataSource, GoogleCloudDataSource, MarketoDataSource, DynamoDBDataSource, \
    HTTPDataSource, TwitterDataSource, ZendeskDataSource, MySQLDataSource, RedshiftDataSource, AmazonS3DataSource, \
    MSSQLDataSource, JiraDataSource, MixpanelDataSource, TeradataDataSource, SFTPDataSource
    HTTPDataSource, TwitterDataSource, ZendeskDataSource, AdwordsDataSource
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
                                  validators=[FileExtensionValidator(allowed_extensions=['json', 'yml', 'xml'])])

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


class OracleDBDataSourceForm(forms.ModelForm):

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
                                                                'placeholder': _('Schema name'),
                                                                'maxlength': 255}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(OracleDBDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = OracleDBDataSource
        fields = ('host', 'port', 'username', 'password', 'database', 'schema_name')


class FTPDataSourceForm(forms.ModelForm):

    host = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('FTP server address'),
               'maxlength': 255}))

    port = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('FTP server port number'),
               'maxlength': 255}))

    username = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Username'),
               'maxlength': 255}))

    password = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Password'),
               'maxlength': 255}))

    prefix = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Prefix of target files'),
               'maxlength': 255}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(FTPDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = FTPDataSource
        fields = ('host', 'port', 'username', 'password', 'prefix')


class MongoDBDataSourceForm(forms.ModelForm):

    uri = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('MongoDB connection string URI'),
               'maxlength': 255}))

    hosts = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('List of hosts(separated by comma)'),
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

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(MongoDBDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = MongoDBDataSource
        fields = ('uri', 'hosts', 'port', 'username', 'password', 'database')


class HadoopDataSourceForm(forms.ModelForm):

    path = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('File path on Hadoop filesystem'),
               'maxlength': 255}))

    os_config_file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-input'}),
                                  validators=[FileExtensionValidator(allowed_extensions=['json', 'yml', 'xml'])])

    os_config_params = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Configuration\'s parameters to overwrite'),
               'maxlength': 255}))

    log_level = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Set log level of Hadoop Parquet reader module'),
               'maxlength': 255}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(HadoopDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = HadoopDataSource
        fields = ('path', 'os_config_file', 'os_config_params', 'log_level')


class SalesforceDataSourceForm(forms.ModelForm):

    username = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Username'),
               'maxlength': 255}))

    password = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Password'),
               'maxlength': 255}))

    endpoint = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Login endpoint URL'),
               'maxlength': 255}))

    sf_object = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('API object\'s name'),
               'maxlength': 255}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(SalesforceDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = SalesforceDataSource
        fields = ('username', 'password', 'endpoint', 'sf_object')


class GoogleCloudDataSourceForm(forms.ModelForm):

    bucket = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('GCS bucket name'),
               'maxlength': 255}))

    paths = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('List of target keys'),
               'maxlength': 255}))

    account_email = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('GCS service account email'),
               'maxlength': 255}))

    private_key = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-input'}),
                                  validators=[FileExtensionValidator(allowed_extensions=['json', 'yml', 'xml'])])

    app_name = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Application name'),
               'maxlength': 255}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(GoogleCloudDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = GoogleCloudDataSource
        fields = ('bucket', 'paths', 'account_email', 'app_name', 'private_key')


class MarketoDataSourceForm(forms.ModelForm):

    endpoint = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('SOAP endpoint URL for your account'),
               'maxlength': 255}))

    account_id = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('User ID'),
               'maxlength': 255}))

    start_time = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Fetch leads since this time'),
               'maxlength': 255}))

    key_file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-input'}),
                                  validators=[FileExtensionValidator(allowed_extensions=['json', 'yml', 'xml'])])

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(MarketoDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = MarketoDataSource
        fields = ('endpoint', 'account_id', 'start_time', 'key_file')


class DynamoDBDataSourceForm(forms.ModelForm):

    host = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Host name'),
               'maxlength': 255}))

    port = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Port number'),
               'maxlength': 255}))

    access_key = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('AWS access key'),
               'maxlength': 255}))

    secret_key = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('AWS secret key'),
               'maxlength': 255}))

    database = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Database name'),
               'maxlength': 255}))

    region = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Region name'),
               'maxlength': 255}))

    endpoint = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Endpoint URL'),
               'maxlength': 255}))

    table = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Table name'),
               'maxlength': 255}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(DynamoDBDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = DynamoDBDataSource
        fields = ('host', 'port', 'access_key', 'secret_key', 'database', 'region', 'endpoint', 'table')


class HTTPDataSourceForm(forms.ModelForm):

    url = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Base url string'),
               'maxlength': 255}))

    method = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('HTTP method'),
               'maxlength': 255}))

    params = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Pairs of name/value to specify query parameters'),
               'maxlength': 255}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(HTTPDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = HTTPDataSource
        fields = ('url', 'method', 'params')


class TwitterDataSourceForm(forms.ModelForm):

    account_id = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('User ID'),
               'maxlength': 255}))

    archive_id = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Archive/Feed ID'),
               'maxlength': 255}))

    archive_link = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Archive/Feed Public Link URL'),
               'maxlength': 255}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(TwitterDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TwitterDataSource
        fields = ('account_id', 'archive_id', 'archive_link')


class ZendeskDataSourceForm(forms.ModelForm):

    login_url = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Login URL for Zendesk'),
               'maxlength': 255}))

    username = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Username'),
               'maxlength': 255}))

    password = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Password'),
               'maxlength': 255}))

    target = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Zendesk export resource type'),
               'maxlength': 255}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(ZendeskDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ZendeskDataSource
        fields = ('login_url', 'username', 'password', 'target')


class MySQLDataSourceForm(forms.ModelForm):

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

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(MySQLDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = MySQLDataSource
        fields = ('host', 'port', 'username', 'password', 'database')


class RedshiftDataSourceForm(forms.ModelForm):

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

    schema_name = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Destination schema name'),
               'maxlength': 255}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(RedshiftDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = RedshiftDataSource
        fields = ('host', 'port', 'username', 'password', 'database', 'schema_name')


class AmazonS3DataSourceForm(forms.ModelForm):

    bucket = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('S3 bucket name'),
               'maxlength': 255}))

    path_prefix = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Prefix of target keys'),
               'maxlength': 255}))

    access_key = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('AWS access key ID'),
               'maxlength': 255}))

    secret_key = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('AWS secret access key'),
               'maxlength': 255}))

    endpoint = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('S3 endpoint login user name'),
               'maxlength': 255}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(AmazonS3DataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = AmazonS3DataSource
        fields = ('bucket', 'path_prefix', 'access_key', 'secret_key', 'endpoint')


class MSSQLDataSourceForm(forms.ModelForm):

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

    instance = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Destination instance name'),
               'maxlength': 255}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(MSSQLDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = MSSQLDataSource
        fields = ('host', 'port', 'username', 'password', 'database', 'instance')


class MixpanelDataSourceForm(forms.ModelForm):

    key = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Project API Key'),
               'maxlength': 255}))

    secret = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Project API Secret'),
               'maxlength': 255}))

    timezone = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Project timezone'),
               'maxlength': 255}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(MixpanelDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = MixpanelDataSource
        fields = ('key', 'secret', 'timezone')


class JiraDataSourceForm(forms.ModelForm):

    uri = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('JIRA API endpoint '),
               'maxlength': 255}))

    username = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Username'),
               'maxlength': 255}))

    password = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Password'),
               'maxlength': 255}))

    jql = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('JQL for extract target issues'),
               'maxlength': 255}))

    issue_columns = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Target issue attributes - key-pair value for attribute\'s name and type'),
               'maxlength': 255}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(JiraDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = JiraDataSource
        fields = ('uri', 'username', 'password', 'jql', 'issue_columns')


class TeradataDataSourceForm(forms.ModelForm):

    host = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('TD host name'),
               'maxlength': 255}))

    username = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('TD username'),
               'maxlength': 255}))

    password = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Password'),
               'maxlength': 255}))

    database = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('TD database name'),
               'maxlength': 255}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(TeradataDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TeradataDataSource
        fields = ('host', 'username', 'password', 'database')


class SFTPDataSourceForm(forms.ModelForm):

    host = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('SFTP server address'),
               'maxlength': 255}))

    port = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('SFTP server port number'),
               'maxlength': 255}))

    username = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Username'),
               'maxlength': 255}))

    password = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Password'),
               'maxlength': 255}))

    prefix = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Prefix of output paths'),
               'maxlength': 255}))

    passphrase = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Secret key passphrase'),
               'maxlength': 255}))

    secret_key = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-input'}),
                                  validators=[FileExtensionValidator(allowed_extensions=['json', 'yml', 'xml'])])

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(SFTPDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = SFTPDataSource
        fields = ('host', 'port', 'username', 'password', 'prefix', 'passphrase', 'secret_key')



class AdwordsDataSourceForm(forms.ModelForm):

    conditions = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Query condition list (e.g. - "CampaignStatus IN")'),
               'maxlength': 255}))

    field_list = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Field list to query'),
               'maxlength': 255}))

    date_range = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Date range'),
               'maxlength': 255}))

    report_type = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-input',
               'placeholder': _('Report type'),
               'maxlength': 255}))

    oauth_key_file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-input'}),
                                     validators=[FileExtensionValidator(allowed_extensions=['json', 'yml', 'xml'])])

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(AdwordsDataSourceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = AdwordsDataSource
        fields = ('conditions', 'field_list', 'date_range', 'report_type', 'oauth_key_file')
