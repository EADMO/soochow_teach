from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Teacher
from .models import Student
# Create your views here.
def form(request):
    template=loader.get_template('form.html')
    return HttpResponse(template.render())
