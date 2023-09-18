from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.template import loader
from django.contrib import messages
from django.db.models import Q
from specialities.form import SpecialitiesCreateForm
from specialities.models import Specialities
from user.models import User


def CreateSpecialities(request):
    context = {}
    template = loader.get_template('../templates/create_specialities.html')
    if request.method == "POST":
        form = SpecialitiesCreateForm(request.POST, request.FILES)
        if form.is_valid():
            specialities = form.save()
            messages.success(request, ('Your specialities was successfully create!'))
            return redirect('specialities_detail', pk=specialities.pk)
        else:
            messages.error(request, 'Error saving form')

        return redirect("/")
    else:
        form = SpecialitiesCreateForm()
        specialities = Specialities.objects.all()
        context['form'] = form
        context['specialities'] = specialities
        return HttpResponse(template.render(context, request))


def index():
    pass


class SearchSpecialities(ListView):
    model = Specialities
    template_name = "../templates/result.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Specialities.objects.filter(
            Q(specialities__Speciality__icontains=query) | Q(specialities__Specialities__icontains=query)
        ).distinct()
        return queryset

def SpecialityEdit(request, pk):
    if request.user.is_authenticated:
        pass

    else:
        return render(request, '../templates/login.html',context={'form':AuthenticationForm()})


def GetSpeciality(request,pk):
    if request.user.is_authenticated:
        template = loader.get_template('../templates/specialities_details.html')
        specialities = Specialities.objects.get(pk=pk)
        context = {'specialities':specialities}
        return HttpResponse(template.render(context, request))
    else:
        return render(request, '../templates/login.html',context={'form':AuthenticationForm()})



def GetAllSpecialities(request):
    if request.user.is_authenticated:
        template = loader.get_template('../templates/specialities_view.html')
        specialities = Specialities.objects.all()
        context = {'specialities':specialities}
        return HttpResponse(template.render(context, request))
    else:
        return render(request, '../templates/login.html',context={'form':AuthenticationForm()})

