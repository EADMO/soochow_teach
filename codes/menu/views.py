from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Teacher
from .models import Student
from random import shuffle
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.
def form(request):
    template=loader.get_template('form.html')
    return HttpResponse(template.render())

def index(request):
    stu_list1 = Student.objects.all().values()[0]
    stu_list2 = Student.objects.all().values()[1]
    template = loader.get_template("index.html")
    context = {
        "stu_list1": stu_list1,
        "stu_list2": stu_list2,
    }
    return HttpResponse(template.render(context, request))

def Err404(req):
    return render(req,'404Error.html')

def login(req):
    return render(req,'login.html')

def loginError(req):
    return render(req,'loginError.html')

def subFail(req):
    return render(req, 'fail.html')

def message(req,stuID):
    try:
        stu = Student.objects.get(pk = stuID)
    except Student.DoesNotExist:
        raise Http404("Student does not exist")
    template = loader.get_template("message.html")
    context = {
        "stu": stu,
    }
    return HttpResponse(template.render(context, req))

def messageForm(req):
    return render(req,'messageForm.html')

def selfFrom(req):
    return render(req,'selfForm.html')

def submit(req):
    try:
        name = req.POST['name']
        gender = req.POST['gender']
        birthday = req.POST['birthday']
        wechat = req.POST['wechat']
        jobStatus = req.POST['job-status']
        identity = req.POST['identity'] #学历
        phone = req.POST['phone']
        email = req.POST['email']
        strengths = req.POST['strengths']
        education = req.POST['education']
        certificates = req.POST['certificates']
        volunteer = req.POST['volunteer']
        dic = {"tom":"student", "name" : "sesese", "gender" : "23333"}
    except Exception as e:
        return render(req,'fail.html')
    else:
        teacher = Teacher(name = name,
                        selfDesc = strengths,
                            edu = identity,
                            sex = gender,
                            wechart_number = wechat,
                            phonenumber = phone,
                            experience = education,
                            mail = email,
                            time = 1,
                            subjects = 'null'
                            )
        teacher.save()
        return render(req,'success.html')
    
def std(request):
    return render(request,'index_student.html')

def tea(request):
    return render(request,'index_teacher.html')

def registerParse(request):
    try:
        username1=request.POST['username']
        password1=request.POST['password']
    except Exception as e:
        return render(request,'fail.html')
    else:
        person=User(username=username1,password=password1)
        person.save()
        return render(request,'success.html')
    
def loginParse(request):
    username1=request.POST['username']
    password1=request.POST['password']
    # print(username1)
    # print(password1)
    # user=authenticate(request,username='zx',password='123')
    # if user is not None:
    return index(request)
    # else:
    #     return render(request,'fail.html')
    
def register(request):
    return render(request,'register.html')

def index_teacher(request):
    return render(request,'index_Teacher.html')

def index_Student(request):
    return render(request,'index_Student.html')