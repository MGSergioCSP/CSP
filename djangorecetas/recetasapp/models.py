from django.db import models
from datetime import date

class Ingrediente(models.Model):
    nome = models.CharField(max_length=255, unique=True, verbose_name="Nome do Ingrediente")

    def __str__(self):
        return self.nome

class Plato(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome do prato")
    tempada = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tempada")
    preparacion = models.TextField(blank=True, null=True, verbose_name="Preparación")
    fotoUrl = models.URLField(max_length=500, blank=True, null=True, verbose_name="URL da foto")

    def __str__(self):
        return f"{self.nome} ({self.tempada})"

class LinaIngrediente(models.Model):
    UNIDADES_CHOICES = [
        ('l', 'Litros'),
        ('ml', 'Mililitros'),
        ('g', 'Gramos'),
        ('kg', 'Quilogramos'),
        ('unidade', 'Unidade(s)'),
        ('cucharada', 'Culleres'),
        ('pizca', 'Pizca'),
        ('taza', 'Cunca')
    ]

    plato = models.ForeignKey(Plato, on_delete=models.CASCADE, related_name='lina_ingredientes', verbose_name="Plato")
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE, verbose_name="Ingrediente")
    cantidade = models.FloatField(verbose_name="Cantidade")
    unidade = models.CharField(max_length=50, choices=UNIDADES_CHOICES, verbose_name="Unidade")

    def __str__(self):
        return f"{self.cantidade} {self.get_unidade_display()} de {self.ingrediente.nome}"

class EntradaMenu(models.Model):
    data = models.DateField(default=date.today, verbose_name="Data do Menú")
    momento = models.CharField(max_length=100, help_text="Ex: Xantar, Cea...", verbose_name="Momento")
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE, related_name='entradas_menu', verbose_name="Plato asignado")

    def __str__(self):
        return f"{self.data.strftime('%d/%m/%Y')} ({self.momento}): {self.plato.nome}"

    class Meta:
        verbose_name = "Entrada do Menú"
        verbose_name_plural = "Entradas do Menú"
        ordering = ['-data']
