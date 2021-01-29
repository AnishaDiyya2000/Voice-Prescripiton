from django.core import validators
from django import forms
from .models import admin_doc


class DocRegistration(forms.ModelForm):
    class Meta:
        model = admin_doc

        fields = ['name1', 'mobile', 'department_doc',
                  'age', 'gender', 'email']
        widgets = {
            'name1': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'department_doc': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),


        }
