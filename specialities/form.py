from django import forms
from django.forms import TextInput, CheckboxInput

from .models import Specialities


class SpecialitiesCreateForm(forms.ModelForm):

    class Meta:
        model = Specialities
        fields= ['Speciality','Specialities','Nnpoa','NC','CF','Tlcnumber','Tlcf','HvfNumber','Hvf','HvfAvrage']
        widgets = {
                    'Speciality': TextInput(attrs={
                       'class': "form-control form-control-lg",
                       'css': 'max-width: 300px;',
                       'placeholder': 'Speciality'
                   }),
                   'Specialities': TextInput(attrs={
                       'class': "form-control form-control-lg",
                       'css': 'max-width: 300px;',
                       'placeholder': "Specialities"
                   }),
        }
        labels = {
            'Speciality': 'Speciality',
            'Specialities': 'Specialities ',
            'Nnpoa':'',
            'NC':'',
            'CF':'',
            'Tlcnumber':'',
            'Tlcf':'',
            'HvfNumber':'',
            'Hvf':'',
            'HvfAvrage':''
        }
