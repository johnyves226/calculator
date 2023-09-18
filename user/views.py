from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import UserSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.template import loader
from contact.models import Service, Speciality, Contact
from contact.form import CreateServiceForm, CreateContactForm, CreateSpecialityForm
from bootstrap_modal_forms.generic import BSModalCreateView

"""def test(request):
    return render(request, '../templates/test.html')
"""


def index(request):
    return render(request, '../templates/index.html')


class add_contact(BSModalCreateView):
    template_name = loader.get_template('../templates/contact_form.html')
    form_class = CreateContactForm
    success_message = 'Success: contact was send.'
    success_url = reverse_lazy('index')
