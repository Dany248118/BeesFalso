from django.urls import path
from . import views
from .views import CrearPromociones

urlpatterns = [
    path('', views.home, name='promociones'),
    path('crearPromocion/', CrearPromociones.as_view(), name='crearPromociones')
]
