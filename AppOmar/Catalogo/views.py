from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from .models import Productos
from .forms import ProductoForm
from django.urls import reverse_lazy

# Create your views here.
class ProductosListView(ListView):
    model = Productos
    template_name = 'Productos.html'
    context_object_name = 'productos'

class CrearProductos (CreateView):
    model = Productos
    template_name = 'Crear_Productos.html'
    context_object_name = 'productos'
    form_class = ProductoForm
    success_url = reverse_lazy('productos')

class EliminarProductos(DeleteView):
    model = Productos
    template_name = 'Eliminar_Productos.html'
    success_url = reverse_lazy('productos')