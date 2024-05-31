from django import forms
from .models import Promociones

class PromoForm(forms.ModelForm):
    class Meta:
        model = Promociones
        fields ='__all__'