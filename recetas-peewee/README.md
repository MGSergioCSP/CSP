# Receitas con Peewee (ORM)

Esta é a implementación da persistencia usando o ORM Peewee para o proxecto `recetas`.

## Requisitos
- Python 3.x
- Librería `peewee`. Esta implementación xa usa SQLite por debaixo, polo que non tes que instalar ningún servidor de base de datos extra.

### Instalación de dependencias
Asegúrate de instalar Peewee na túa contorna:

```bash
pip install peewee
```

## Como Executar
Na mesma carpeta, executa o script de test:

```bash
python main.py
```

Isto inicializará unha base de datos SQLite chamada `recetas_peewee.db`, na que se gardarán obxectos coma instanciacións de Peewee, reflectindo o paradigma *Active Record*.

## Estrutura
- **modelos.py**: Controi e define as clases, que herdan de `peewee.Model`. Agrupan tanto os datos como os métodos de control e asociación entre clases (p.ex., chaves foráneas de `LinaIngrediente` a `Plato`). Inclúese a lóxica orixinal adaptada a métodos de gardado con ORM (como o `.save()` natural das clases, e un `.create()`).
- **main.py**: Ficheiro principal para confirmar e visualizar o funcionamento do ORM gardando un prato na base de datos e comprobándoo despois.
