from django.contrib import admin
from django.db import models
from .models import modelForm
# Register your models here.
class viewForm(admin.ModelAdmin):
    list_display = ['id','name', 'email', 'password']


admin.site.register(modelForm, viewForm)