# External imports
from django.contrib import admin

# Internal imports
from .models import Question, Choice

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
