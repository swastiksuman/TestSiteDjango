__author__ = 'Alien'

from django import forms

class EmailForm(forms.Form):

    name = forms.CharField(required=False)
    email = forms.EmailField()
    ip_address = forms.CharField(required=False)



