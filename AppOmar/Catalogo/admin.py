from django.contrib import admin
from . models import Productos
from django.utils.html import format_html

# Register your models here.
class ProductosAdmin(admin.ModelAdmin):
    list_display = (
        'precio',
        'marca',
        'categoria',
        'retornable',
        'tamaño_embalaje',
        'existencias',
        'foto',
    )

    def foto(self, obj):
        return format_html('<img src={} width="130" height="100"/>', obj.imagen.url)

admin.site.register(Productos, ProductosAdmin)    