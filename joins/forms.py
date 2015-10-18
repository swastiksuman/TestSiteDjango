__author__ = 'Alien'

from django import forms

class EmailForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

