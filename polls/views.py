# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, You'ar at the polls index.")


def contact(request):
    return HttpResponse("Hello, You'ar at the polls Contact page.")


def test(request):
    return HttpResponse("Hello, You'ar at the polls Test page.")