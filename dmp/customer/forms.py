from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from customer.models import Profile


class UserAuthenticationForm(AuthenticationForm):
    error_messages = {
        'inactive': _("Please confirm your email address before login"),
        'invalid_login': _("Your username and password didn't match. Please try again.")
    }

    username = forms.EmailField(max_length=60,
                                widget=forms.EmailInput(attrs={'class': 'form-input',
                                                               'placeholder': _('Email Address'),
                                                               'maxlength': 60
                                                               }),
                                error_messages={'invalid': 'Please enter a valid email address'})
    password = forms.CharField(max_length=128,
                               strip=False,
                               widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                 'placeholder': _('Password'),
                                                                 'maxlength': 128
                                                                 }))

    def __init__(self, *args, **kwargs):
        super(UserAuthenticationForm, self).__init__(*args, **kwargs)


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=120, required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-input',
                                                               'placeholder': _('First Name'),
                                                               'maxlength': 120}),
                                 error_messages={'invalid': 'Please enter a valid email address'})
    last_name = forms.CharField(max_length=120, required=False,
                                widget=forms.TextInput(attrs={'class': 'form-input',
                                                              'placeholder': _('Last Name'),
                                                              'maxlength': 120}))

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name')
