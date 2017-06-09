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

    def get_template_names(self):
        templates = super(DataSourceCreateView, self).get_template_names()
        try:
            provider = DataProvider.objects.get(id=self.kwargs.get('provider_id'))
            templates.insert(0, 'datasource/datasource_forms/{template_name}.html'.format(template_name=provider.name))
        except DataProvider.DoesNotExist:
            pass
        return templates

    def form_valid(self, form):
        data_source = form.save(commit=False)
        data_source.user = self.request.user
        data_source.data_provider_id = self.kwargs.get('provider_id')
        form = super(DataSourceCreateView, self).form_valid(form)
        return form


    # def get_form_kwargs(self):
    #     kwargs = super(DataSourceCreateView, self).get_form_kwargs()
    #     kwargs.update(instance={
    #         'data_source': self.object,
    #         'analytics_data_source': AnalyticsDataSource.objects.get(data_source__pk=self.object.pk),
    #     })
    #     return kwargs

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
