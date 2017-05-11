from django.conf.urls import url

from customer.views import LoginView, LogoutView, ProfileUpdateView

urlpatterns = [
    url(r'login/', LoginView.as_view(), name='login'),
    url(r'logout/', LogoutView.as_view(), name='logout'),
    url(r'profile/', ProfileUpdateView.as_view(), name='profile'),
]

