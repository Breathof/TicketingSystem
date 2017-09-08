from django.contrib.auth.models import User
from django import forms
import django_filters

from .models import Ticket


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password"]


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['title', 'body', 'status', 'user']


class TicketFilter(django_filters.FilterSet):

    class Meta:
        model = Ticket
        fields = ['title', 'status']

