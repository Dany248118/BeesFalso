from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf import settings
from django.urls import path
from . import views
from .views import ProductosListView, CrearProductos, EliminarProductos

urlpatterns = [
    path('', ProductosListView.as_view(), name='productos'),
    path('nuevoProducto/', CrearProductos.as_view(), name='crearProductos'),
    path('eliminarProducto/<int:pk>', EliminarProductos.as_view(), name='eliminarProducto')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)