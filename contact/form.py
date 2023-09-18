from django import forms
from django.forms import TextInput, CheckboxInput
from django.forms import ModelChoiceField

from bootstrap_modal_forms.forms import BSModalModelForm

from .models import Contact, Service,Speciality,Object


class CreateSpecialityForm(forms.ModelForm):
    class Meta:
        model = Speciality
        fields = ['name']


class CreateServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name']


class CreateContactForm(BSModalModelForm):
    demande_object = forms.ModelChoiceField(Object.objects.all())
    class Meta:
        model = Contact
        fields = ['first_name' ,'last_name' , 'email' ,'phone_number' ,'phone_number2' ,'speciality' ,'location' ,'services' ,'demande_object' ]

