from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Promociones
from .forms import PromoForm
from django.urls import reverse_lazy

# Create your views here.
class CrearPromociones(CreateView):
    model = Promociones
    template_name = 'Crear_Promocion.html'
    context_object_name = 'promociones'

def home(request):
    return render(request, 'Promociones.html')