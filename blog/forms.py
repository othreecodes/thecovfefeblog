from django import forms
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import User
from django.core.exceptions import ImproperlyConfigured
from django.utils.module_loading import import_string
from django.utils.translation import ugettext_lazy as _


class UserForm(forms.ModelForm):
    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }

    username = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'class': 'form-control', 'type': 'email'}))

    password = forms.CharField(label=_("Password"),
                                widget=forms.PasswordInput(attrs={'required': True, 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
