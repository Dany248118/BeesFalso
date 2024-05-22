from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'main'),
    path('login/', views.login, name= 'iniciar')
]
