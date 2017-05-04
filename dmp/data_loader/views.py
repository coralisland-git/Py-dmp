from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from data_loader.models import DataSource
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy


class DataSourceListView(LoginRequiredMixin, ListView):
    login_url = '/customer/login/'
    model = DataSource
    template_name = 'datasource/datasource_list.html'


class DataSourceCreateView(CreateView):
    model = DataSource
    fields = ('title', 'data_source', 'upload_file')
    template_name = 'datasource/datasource_create.html'


class DataSourceUpdateView(UpdateView):
    model = DataSource


class DataSourceDeleteView(DeleteView):
    model = DataSource
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse('index')


class DataProviderListView(ListView):
    queryset = DataSource.objects.all()
    template_name = 'datasource/data_providers_list.html'
