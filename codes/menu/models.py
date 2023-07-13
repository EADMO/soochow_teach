from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20,default="noone")
    salary=models.IntegerField(default=0)
    selfDesc=models.CharField(max_length=100,default="")
    subject=models.CharField(max_length=20,default="")
    w_sex=models.CharField(max_length=20,default="")
    age=models.CharField(max_length=20,default="")
    w_edu=models.CharField(max_length=20,default="")
    w_time=models.IntegerField(default=0)
    mail=models.CharField(max_length=50,default="")
    address=models.CharField(max_length=100,default="")
    grade=models.CharField(max_length=20,default="")
    def __str__(self) -> str:
        return ' '.join([self.name, self.age, self.w_edu, self.subject])

class Teacher(models.Model):
    name = models.CharField(max_length=20,default="Anonymous")
    salary = models.PositiveIntegerField(default=0)
    selfDesc = models.CharField(max_length=100,default='')
    subjects = models.CharField(max_length=20)
    sex = models.CharField(max_length=4, default="Null")
    edu = models.CharField(max_length=20,default='Null')
    time = models.PositiveIntegerField()
    mail = models.CharField(max_length=30)
    wechart_number=models.IntegerField()
    phonenumber=models.IntegerField()
    experience=models.CharField(max_length=50)
    def __str__(self) -> str:
        return ' '.join([self.name, self.edu, self.subjects])
