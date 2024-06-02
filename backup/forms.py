from django import forms
from .models import Confiback
from django.contrib import admin
from django.forms import ModelForm, PasswordInput


class ConfibackAdminForm(forms.ModelForm):
  class Meta:
    model =Confiback
    widgets = {
      'password' : forms.PasswordInput
    }

    fields = '__all__'












