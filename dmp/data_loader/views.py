from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from data_loader.models import DataSource
from django.contrib.auth.mixins import LoginRequiredMixin


class DataSourceListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = DataSource
    template_name = 'datasource/datasource_list.html'


class DataSourceCreateView(CreateView):
    model = DataSource


class DataSourceUpdateView(UpdateView):
    model = DataSource