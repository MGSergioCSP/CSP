# Proxecto Django: djangorecetas

Este proxecto foi creado dende cero cumprindo as especificacións para desenvolver un aplicación web cos menús semanais e receitas (POO aplicado á Web con Django DB ORM `SQLite`).

## Especificacións Imprimentadas
- **Modelo Relacional**: O esquema ORM mapéase á mesma lóxica orixinal do deseño POO (Ingrediente, Plato, LiñaIngrediente e EntradaMenu).
- **Control Fóra de Admin**: Toda a aplicación pódese utilizar independentemente do panel de aministración, con vistas para ler, crear, editar e borrar pratos.
- **Formularios Automatizados**: Usados `forms.ModelForm` base.
- **Deseño y Herdanza de Templates**: Toda a fachada parte do template `base.html`. Fíxose uso da libraría externa de estilos Bootstrap CDN. Empregáronse varias Etiquetas ("tags") como `{% url %}`, `{% for %}`, `{% if %}`, `{% extends %}`, `{% regroup %}`. Tamén se utilizaron filtros ("filters") como `|title`, `|date`, `|default`, `|slice` nas listaxes de datos.
- **Admin Persoal**: `sergiom`

## Como Comezar / Despregamento Local

1. Clona/Descarga o repositorio.
2. Na carpeta `djangorecetas`, asegura de instalar as dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Fai as migracións de comprobación (aínda que a bd xa inclúese configurada por defecto cun superuser se mantés o arquivo db.sqlite3 provisto):
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Levanta o servidor en local:
   ```bash
   python manage.py runserver
   ```
5. Abre o navegador en [http://localhost:8000](http://localhost:8000).

Para o panel de administración diríxete a [http://localhost:8000/admin](http://localhost:8000/admin) cas credenciais:
- **Usuario**: `sergiom`
- **Contrasinal**: `sergiom`
