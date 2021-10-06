#  external imports
from django.urls import path

# Internal imports
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact_us/', views.contact, name='contact' ),
    path('test/', views.test, name='test'),
]
