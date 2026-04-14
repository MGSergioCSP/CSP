from django import forms
from .models import Plato, Ingrediente, EntradaMenu

class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = ['nome', 'tempada', 'preparacion', 'fotoUrl']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'tempada': forms.TextInput(attrs={'class': 'form-control'}),
            'preparacion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fotoUrl': forms.URLInput(attrs={'class': 'form-control'}),
        }

class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EntradaMenuForm(forms.ModelForm):
    class Meta:
        model = EntradaMenu
        fields = ['data', 'momento', 'plato']
        widgets = {
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'momento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Xantar, Cea...'}),
            'plato': forms.Select(attrs={'class': 'form-select'}),
        }
