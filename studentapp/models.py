from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login(models.Model):
    username =models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()


class School(models.Model):
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
       return self.name

class Course(models.Model):
      name = models.CharField(max_length=200)
      def __str__(self):
        return self.name

class Student(models.Model):

    name= models.CharField(max_length=100)
    address= models.TextField(max_length=200)
    school= models.ForeignKey(School, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
