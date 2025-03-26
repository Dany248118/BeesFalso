from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'main'),
    path('login/', views.login_view, name= 'iniciar'),
    path('logout/', views.salir, name= 'logout'),
    path('iniciar/', views.Iniciar, name= 'login'),
]
