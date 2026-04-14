from django.shortcuts import render, get_object_or_404, redirect
from .models import Plato, Ingrediente, EntradaMenu
from .forms import PlatoForm, IngredienteForm, EntradaMenuForm

def home(request):
    return render(request, 'home.html')

# --- Pratos ---

def plato_list(request):
    platos = Plato.objects.all()
    return render(request, 'recetasapp/plato_list.html', {'platos': platos})

def plato_detail(request, pk):
    plato = get_object_or_404(Plato, pk=pk)
    return render(request, 'recetasapp/plato_detail.html', {'plato': plato})

def plato_create(request):
    if request.method == 'POST':
        form = PlatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plato_list')
    else:
        form = PlatoForm()
    return render(request, 'recetasapp/plato_form.html', {'form': form, 'title': 'Engadir Plato'})

def plato_update(request, pk):
    plato = get_object_or_404(Plato, pk=pk)
    if request.method == 'POST':
        form = PlatoForm(request.POST, instance=plato)
        if form.is_valid():
            form.save()
            return redirect('plato_list')
    else:
        form = PlatoForm(instance=plato)
    return render(request, 'recetasapp/plato_form.html', {'form': form, 'title': 'Editar Plato'})

def plato_delete(request, pk):
    plato = get_object_or_404(Plato, pk=pk)
    if request.method == 'POST':
        plato.delete()
        return redirect('plato_list')
    return render(request, 'recetasapp/plato_confirm_delete.html', {'plato': plato})


# --- Ingredientes ---

def ingrediente_list(request):
    ingredientes = Ingrediente.objects.all()
    return render(request, 'recetasapp/ingrediente_list.html', {'ingredientes': ingredientes})

def ingrediente_create(request):
    if request.method == 'POST':
        form = IngredienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingrediente_list')
    else:
        form = IngredienteForm()
    return render(request, 'recetasapp/ingrediente_form.html', {'form': form, 'title': 'Engadir Ingrediente'})

def ingrediente_delete(request, pk):
    ingrediente = get_object_or_404(Ingrediente, pk=pk)
    if request.method == 'POST':
        ingrediente.delete()
        return redirect('ingrediente_list')
    return render(request, 'recetasapp/ingrediente_confirm_delete.html', {'ingrediente': ingrediente})


# --- Entrada Menu ---

def menu_list(request):
    entradas = EntradaMenu.objects.all()
    return render(request, 'recetasapp/menu_list.html', {'entradas': entradas})

def menu_create(request):
    if request.method == 'POST':
        form = EntradaMenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = EntradaMenuForm()
    return render(request, 'recetasapp/menu_form.html', {'form': form, 'title': 'Planificar Novo Menú'})

def menu_delete(request, pk):
    entrada = get_object_or_404(EntradaMenu, pk=pk)
    if request.method == 'POST':
        entrada.delete()
        return redirect('menu_list')
    return render(request, 'recetasapp/menu_confirm_delete.html', {'entrada': entrada})
