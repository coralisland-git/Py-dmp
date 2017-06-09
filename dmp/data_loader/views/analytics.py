# class DataSourceCreateView(LoginRequiredMixin, CreateView):
#     model = DataSource
#     form_class = DataSourceCreateForm
#     template_name = 'datasource/datasource_create.html'
#     success_url = reverse_lazy('index')
#
#     def get_template_names(self):
#         templates = super(DataSourceCreateView, self).get_template_names()
#         try:
#             provider = DataProvider.objects.get(id=self.kwargs.get('provider_id'))
#             templates.insert(0, 'datasource/datasource_forms/{template_name}.html'.format(template_name=provider.name))
#         except DataProvider.DoesNotExist:
#             pass
#         return templates
#
#     def form_valid(self, form):
#         data_source = form.save(commit=False)
#         data_source.user = self.request.user
#         data_source.data_provider_id = self.kwargs.get('provider_id')
#         form = super(DataSourceCreateView, self).form_valid(form)
#         return form
#
#
#     # def get_form_kwargs(self):
#     #     kwargs = super(DataSourceCreateView, self).get_form_kwargs()
#     #     kwargs.update(instance={
#     #         'data_source': self.object,
#     #         'analytics_data_source': AnalyticsDataSource.objects.get(data_source__pk=self.object.pk),
#     #     })
#     #     return kwargs
#
#     def get_context_data(self, **kwargs):
#         context = super(DataSourceCreateView, self).get_context_data(**kwargs)
#         provider = DataProvider.objects.get(id=self.kwargs.get('provider_id'))
#         context['provider'] = provider
#         return context
#
#
# class DataSourceUpdateView(LoginRequiredMixin, UpdateView):
#     model = DataSource
#     form_class = DataSourceCreateForm
#     template_name = 'datasource/datasource_create.html'
#     success_url = reverse_lazy('index')
#
#     def get_template_names(self):
#         templates = super(DataSourceUpdateView, self).get_template_names()
#         try:
#             provider = DataProvider.objects.get(id=self.object.data_provider.id)
#             templates.insert(0, 'datasource/datasource_forms/{template_name}.html'.format(template_name=provider.name))
#         except DataProvider.DoesNotExist:
#             pass
#         return templates
#
#     def get_context_data(self, **kwargs):
#         context = super(DataSourceUpdateView, self).get_context_data(**kwargs)
#         provider = DataProvider.objects.get(id=self.object.data_provider.id)
#         context['provider'] = provider
#         return context
#
#
#
# class RecipeCreateView(CreateView):
#     template_name = 'recipe_add.html'
#     model = Recipe
#     form_class = RecipeForm
#     success_url = 'success/'
#
#     def get(self, request, *args, **kwargs):
#         """
#         Handles GET requests and instantiates blank versions of the form
#         and its inline formsets.
#         """
#         self.object = None
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         ingredient_form = IngredientFormSet()
#         instruction_form = InstructionFormSet()
#         return self.render_to_response(
#             self.get_context_data(form=form,
#                                   ingredient_form=ingredient_form,
#                                   instruction_form=instruction_form))
#
#     def post(self, request, *args, **kwargs):
#         """
#         Handles POST requests, instantiating a form instance and its inline
#         formsets with the passed POST variables and then checking them for
#         validity.
#         """
#         self.object = None
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         ingredient_form = IngredientFormSet(self.request.POST)
#         instruction_form = InstructionFormSet(self.request.POST)
#         if (form.is_valid() and ingredient_form.is_valid() and
#             instruction_form.is_valid()):
#             return self.form_valid(form, ingredient_form, instruction_form)
#         else:
#             return self.form_invalid(form, ingredient_form, instruction_form)
#
#     def form_valid(self, form, ingredient_form, instruction_form):
#         """
#         Called if all forms are valid. Creates a Recipe instance along with
#         associated Ingredients and Instructions and then redirects to a
#         success page.
#         """
#         self.object = form.save()
#         ingredient_form.instance = self.object
#         ingredient_form.save()
#         instruction_form.instance = self.object
#         instruction_form.save()
#         return HttpResponseRedirect(self.get_success_url())
#
#     def form_invalid(self, form, ingredient_form, instruction_form):
#         """
#         Called if a form is invalid. Re-renders the context data with the
#         data-filled forms and errors.
#         """
#         return self.render_to_response(
#             self.get_context_data(form=form,
#                                   ingredient_form=ingredient_form,
#                                   instruction_form=instruction_form))
#
#
#
#
#
