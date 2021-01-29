from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    REQUIRED_FIELDS = ['first_name']


class Department(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Doctor(models.Model):

    mobile = models.CharField(max_length=10)
    department = models.ForeignKey(to=Department, on_delete=models.PROTECT)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    user = models.ForeignKey(to=User, on_delete=models.PROTECT)


class Admin(models.Model):
    ad_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Patient(models.Model):

    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)


class Prescription(models.Model):
    diagnosis = models.CharField(max_length=50)
    medicine = models.CharField(max_length=50)
    time = models.CharField(max_length=60)
    advice = models.CharField(max_length=60)
    patient = models.ForeignKey(to=Patient, on_delete=models.PROTECT)


class admin_doc(models.Model):
    name1 = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    department_doc = models.CharField(max_length=50)
    age = models.IntegerField(default=25)
    gender = models.CharField(max_length=10)

    email = models.EmailField(max_length=100)
