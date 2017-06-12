from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from data_loader.models import DataSource, DataProvider, DataFlowSettings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from data_loader.forms import DataSourceCreateForm, DataFlowSettingsForm


class DataSourceListView(LoginRequiredMixin, ListView):
    login_url = '/customer/login/'
    model = DataSource
    template_name = 'datasource/datasource_list.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class DataSourceCreateView(LoginRequiredMixin, CreateView):
    model = DataSource
    form_class = DataSourceCreateForm
    template_name = 'datasource/datasource_create.html'
    success_url = reverse_lazy('index')

    def get_details_form_class(self):
        return None

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
            self.get_context_data(form=form,
                                  details_form=self.get_details_form_class()))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        details_form = self.get_details_form_class()

        # TODO: Refactor this after all datasources will be added
        if details_form:
            details_form = details_form(self.request.POST, self.request.FILES)
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
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
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
        return form

    def form_invalid(self, form, details_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  details_form=details_form))

    def get_template_names(self):
        templates = super(DataSourceCreateView, self).get_template_names()
        try:
            provider = DataProvider.objects.get(id=self.kwargs.get('provider_id'))
            templates.insert(0, 'datasource/datasource_forms/{template_name}.html'.format(template_name=provider.name))
        except DataProvider.DoesNotExist:
            pass
        return templates

    def get_context_data(self, **kwargs):
        context = super(DataSourceCreateView, self).get_context_data(**kwargs)
        provider = DataProvider.objects.get(id=self.kwargs.get('provider_id'))
        context['provider'] = provider
        return context


class DataSourceUpdateView(LoginRequiredMixin, UpdateView):
    model = DataSource
    form_class = DataSourceCreateForm
    template_name = 'datasource/datasource_create.html'
    success_url = reverse_lazy('index')

    def get_template_names(self):
        templates = super(DataSourceUpdateView, self).get_template_names()
        try:
            provider = DataProvider.objects.get(id=self.object.data_provider.id)
            templates.insert(0, 'datasource/datasource_forms/{template_name}.html'.format(template_name=provider.name))
        except DataProvider.DoesNotExist:
            pass
        return templates

    def get_context_data(self, **kwargs):
        context = super(DataSourceUpdateView, self).get_context_data(**kwargs)
        provider = DataProvider.objects.get(id=self.object.data_provider.id)
        context['provider'] = provider
        return context


class DataSourceDeleteView(LoginRequiredMixin, DeleteView):
    model = DataSource
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse('index')


class DataProviderListView(LoginRequiredMixin, ListView):
    model = DataProvider
    template_name = 'datasource/data_providers_list.html'


class DataFlowSettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = DataFlowSettings
    form_class = DataFlowSettingsForm
    success_url = reverse_lazy('index')
    template_name = 'settings.html'

    def get_object(self, queryset=None):
        settings, created = DataFlowSettings.objects.get_or_create(user=self.request.user)
        return settings
