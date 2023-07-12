from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Teacher
from .models import Student
from random import shuffle
# Create your views here.
def form(request):
    template=loader.get_template('form.html')
    return HttpResponse(template.render())

def index(request):
    stu_list = shuffle(Student.objects.all()[:4])
    template = loader.get_template("index.html")
    context = {
        "stu_list": stu_list,
    }
    return HttpResponse(template.render(context, request))

def Err404(req):
    return render(req,'404Error.html')

def login(req):
    return render(req,'loginError.html')

def message(req,stuID):
    try:
        stu = Student.objects.get(pk = stuID)
    except Student.DoesNotExist:
        raise Http404("Student does not exist")
    template = loader.get_template("index.html")
    context = {
        "stu": stu,
    }
    return HttpResponse(template.render(context, req))

def messageForm(req):
    return render(req,'messageForm.html')

def selfFrom(req):
    return render(req,'selfForm.html')
