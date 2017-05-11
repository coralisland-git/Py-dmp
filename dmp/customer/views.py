from django.utils.http import is_safe_url
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView, UpdateView
from django.views.generic.edit import UpdateView
from django.urls import reverse, reverse_lazy
from customer.forms import UserAuthenticationForm, UserProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from customer.models import Profile



class LoginView(FormView):
    """
    Provides the ability to login as a user with a username and password
    """

    form_class = UserAuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'login.html'
    success_url = 'data_loader:datasource-list'

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = reverse(self.success_url)
        return redirect_to


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = 'customer:login'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse(self.url)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = UserProfileForm
    template_name = 'profile.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
