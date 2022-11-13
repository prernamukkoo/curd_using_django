from django import forms
from .models import *
 
class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields=('name','age','email','about')
