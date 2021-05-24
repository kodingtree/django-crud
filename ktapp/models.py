from django.db import models
# from django.forms import forms




# Create your models here.
class modelForm(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=100)