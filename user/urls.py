from django.urls import path
from user import views


urlpatterns = [

     path('',views.index, name='index'),
     path('create/', views.add_contact.as_view(), name='create_contact'),
]
