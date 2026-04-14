from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('platos/', views.plato_list, name='plato_list'),
    path('platos/novo/', views.plato_create, name='plato_create'),
    path('platos/<int:pk>/', views.plato_detail, name='plato_detail'),
    path('platos/<int:pk>/editar/', views.plato_update, name='plato_update'),
    path('platos/<int:pk>/borrar/', views.plato_delete, name='plato_delete'),

    path('ingredientes/', views.ingrediente_list, name='ingrediente_list'),
    path('ingredientes/novo/', views.ingrediente_create, name='ingrediente_create'),
    path('ingredientes/<int:pk>/borrar/', views.ingrediente_delete, name='ingrediente_delete'),

    path('menu/', views.menu_list, name='menu_list'),
    path('menu/novo/', views.menu_create, name='menu_create'),
    path('menu/<int:pk>/borrar/', views.menu_delete, name='menu_delete'),
]
