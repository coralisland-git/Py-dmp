from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from data_loader.models import DataSource, DataProvider, DataFlowSettings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from data_loader.forms import DataSourceCreateForm, DataFlowSettingsForm
from django.shortcuts import get_object_or_404


class DataSourceListView(LoginRequiredMixin, ListView):
    """
    Used to list DataSources in UI for home page.
    """
    login_url = '/customer/login/'
    model = DataSource
    template_name = 'datasource/datasource_list.html'

    def get_queryset(self):
        """
        Returns modified queryset to obtain set of DataSources
        by user.
        :return:
         Set of DataSource models associated with
         authorized user.
        """
        return self.model.objects.filter(user=self.request.user)


class DataSourceCreateView(LoginRequiredMixin, CreateView):
    """
    Used to create DataSource object - render and validate
    DataSource and detailed data source object, save
    both basic and detailed data source objects.
    Might be inherited for particular Data source model.
    """
    model = DataSource
    detailed_model = None
    form_class = DataSourceCreateForm
    template_name = 'datasource/datasource_create.html'
    success_url = reverse_lazy('index')
    details_model_class = None

    def get_detailed_data_source_object(self):
        return None
        # return self.details_model_class.objects.get(id=self.object.id)

    def get_details_form_class(self):
        """
        Basic method to initialize form for concrete DataSource
        :return:
         1. None for general parent DataSource view
         2. Form class for particular DataSource (i.e. Analytics,
          Spreadsheets etc.)
        """
        return None

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests, instantiating a DataSource form instance
        and details_form for concrete DataSource and then renders them
        for UI.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        details_form = self.get_details_form_class()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  details_form=details_form(request=request)))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a DataSource form instance
        and details_form for concrete DataSource with the passed
        POST variables and then checking them for validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        details_form = self.get_details_form_class()

        # TODO: Refactor this after all datasources will be added
        if details_form:
            details_form = details_form(self.request.POST, self.request.FILES, request=request)
            if form.is_valid() and details_form.is_valid():
                return self.form_valid(form, details_form)
            else:
                return self.form_invalid(form, details_form)
        else:
            if form.is_valid():
                return self.form_valid(form, details_form)
            else:
                return self.form_invalid(form, details_form)

    def form_valid(self, form, details_form):
        """
        Called if both form and details_form are valid.
        Creates a DataSource instance along with associated detailed
        datasource data object and then redirects to a success page.
        """
        data_source = form.save(commit=False)
        data_source.user = self.request.user
        data_source.data_provider_id = self.kwargs.get('provider_id')
        data_source.save()
        if details_form:
            detailed_data_source = details_form.save(commit=False)
            detailed_data_source.data_source = data_source
            detailed_data_source.save()
        form = super(DataSourceCreateView, self).form_valid(form)
        if details_form:
            detailed_data_source.create_config_file()
        return form

    def form_invalid(self, form, details_form):
        """
        Called if any form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  details_form=details_form))

    def get_template_names(self):
        """
        Checks if template for form UI is exists and
        adds it's name to set of templates with
        highest priority
        :return:
         Set of template names including form template
         associated with current DataProvider
        """
        templates = super(DataSourceCreateView, self).get_template_names()
        try:
            provider = DataProvider.objects.get(id=self.kwargs.get('provider_id'))
            templates.insert(0, 'datasource/datasource_forms/{template_name}.html'.format(template_name=provider.name))
        except DataProvider.DoesNotExist:
            pass
        return templates

    def get_context_data(self, **kwargs):
        """
        Updates context object with DataProvider object
        to be used in form template
        :param kwargs:
        :return:
         Updated context object
        """
        context = super(DataSourceCreateView, self).get_context_data(**kwargs)
        provider = DataProvider.objects.get(id=self.kwargs.get('provider_id'))
        context['provider'] = provider
        return context


class DataSourceUpdateView(LoginRequiredMixin, UpdateView):
    """
    Used to update existing DataSource object - render and validate
    DataSource and detailed data source object, make updates for
    both basic and detailed data source objects.
    Might be inherited for particular Data source model.
    """
    model = DataSource
    form_class = DataSourceCreateForm
    template_name = 'datasource/datasource_create.html'
    success_url = reverse_lazy('index')


    def get_details_form_class(self):
        """
        Basic method to initialize form for concrete DataSource
        :return:
         1. None for general parent DataSource view
         2. Form class for particular DataSource (i.e. Analytics,
          Spreadsheets etc.)
        """
        return None

    def get_object(self, queryset=None):
        return get_object_or_404(DataSource, pk=self.kwargs['pk'])

    def get_detailed_data_source_object(self):
        return None

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests, instantiating a DataSource form instance
        and details_form for concrete DataSource and then renders them
        for UI.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        details_form = self.get_details_form_class()
        if self.get_detailed_data_source_object():
            details_form = details_form(instance=self.get_detailed_data_source_object(), request=request)
        return self.render_to_response(
            self.get_context_data(form=form,
                                  details_form=details_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a DataSource form instance
        and details_form for concrete DataSource with the passed
        POST variables and then checking them for validity.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        details_form = self.get_details_form_class()

        # TODO: Refactor this after all datasources will be added
        if details_form:
            details_form = details_form(self.request.POST, self.request.FILES, instance=self.get_detailed_data_source_object(), request=request)
            if form.is_valid() and details_form.is_valid():
                return self.form_valid(form, details_form)
            else:
                return self.form_invalid(form, details_form)
        else:
            if form.is_valid():
                return self.form_valid(form, details_form)
            else:
                return self.form_invalid(form, details_form)

    def form_valid(self, form, details_form):
        """
        Called if both form and details_form are valid.
        Creates a DataSource instance along with associated detailed
        datasource data object and then redirects to a success page.
        """
        data_source = form.save(commit=False)
        if details_form:
            detailed_data_source = details_form.save(commit=False)
            detailed_data_source.data_source = data_source
            detailed_data_source.save()
        form = super(DataSourceUpdateView, self).form_valid(form)
        if details_form:
            detailed_data_source.update_config_file()
        return form

    def form_invalid(self, form, details_form):
        """
        Called if any form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  details_form=details_form))

    def get_template_names(self):
        """
        Checks if template for form UI is exists and
        adds it's name to set of templates with
        highest priority
        :return:
         Set of template names including form template
         associated with current DataProvider
        """
        templates = super(DataSourceUpdateView, self).get_template_names()
        try:
            provider = DataProvider.objects.get(id=self.object.data_provider.id)
            templates.insert(0, 'datasource/datasource_forms/{template_name}.html'.format(template_name=provider.name))
        except DataProvider.DoesNotExist:
            pass
        return templates

    def get_context_data(self, **kwargs):
        """
        Updates context object with DataProvider object
        to be used in form template
        :param kwargs:
        :return:
         Updated context object
        """
        context = super(DataSourceUpdateView, self).get_context_data(**kwargs)
        provider = DataProvider.objects.get(id=self.object.data_provider.id)
        context['provider'] = provider
        return context


class DataSourceDeleteView(LoginRequiredMixin, DeleteView):
    """
    Deletes DataSource object from database by it's id
    """
    model = DataSource
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse('index')


class DataProviderListView(LoginRequiredMixin, ListView):
    """
    Renders DataProviders list
    """
    model = DataProvider
    template_name = 'datasource/data_providers_list.html'


class DataFlowSettingsUpdateView(LoginRequiredMixin, UpdateView):
    """
    Updates UserProfile-related settings (like sync_interval etc)
    """
    model = DataFlowSettings
    form_class = DataFlowSettingsForm
    success_url = reverse_lazy('index')
    template_name = 'settings.html'

    def get_object(self, queryset=None):
        """
        Takes or creates (if not exists) Settings object for authorized user
        :param queryset:
        :return:
         Settings object for currently authorized user
        """
        settings, created = DataFlowSettings.objects.get_or_create(user=self.request.user)
        return settings
