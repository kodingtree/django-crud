from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'home'),
    path('submit/', views.subForm),
    path('delete/<int:id>/', views.delData, name='deletedata'),
    path('update/<int:pid>/', views.upData, name='updata')
]
