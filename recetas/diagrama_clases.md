# Diagrama de Clases (Modificado)

```mermaid
classDiagram
    class ElementoMenu {
        <<abstract>>
        +mostrar_info()* string
    }

    class Plato {
        -string _nome
        -string _tempada
        -string _preparacion
        -string _fotoUrl
        -List~LinaIngrediente~ _ingredientes
        +__init__(nome, tempada, preparacion, fotoUrl)
        +engadirIngrediente(LinaIngrediente lina)
        +mostrar_info() string
        +get_nome() string
        +__str__() string
    }
    ElementoMenu <|-- Plato

    class Ingrediente {
        -string __nome
        +__init__(nome)
        +get_nome() string
        +crear_dende_string(nome)$ Ingrediente
        +__str__() string
    }

    class LinaIngrediente {
        -float _cantidade
        -string _unidade
        -Ingrediente _ingrediente
        +__init__(cantidade, unidade, ingrediente)
        +get_ingrediente() Ingrediente
        +validar_unidade(unidade)* bool
        +__str__() string
    }

    class EntradaMenu {
        -date _data
        -string _momento
        -Plato _plato
        +__init__(data, momento, plato)
        +__str__() string
    }

    class XestorMenu {
        -List~EntradaMenu~ __entradas
        +__init__()
        +xestionar(EntradaMenu entrada)
        +procurarPorSemana(date inicio) List~EntradaMenu~
        +procurarPorIngrediente(string nome) List~EntradaMenu~
        +__str__() string
    }

    XestorMenu "1" *-- "*" EntradaMenu : xestiona
    EntradaMenu "1" o-- "1" Plato : asigna
    Plato "1" *-- "*" LinaIngrediente : composición
    LinaIngrediente "1" o-- "1" Ingrediente : referencia
```

## Xustificación das modificacións:
- **ElementoMenu (`Clase Abstracta`)**: Creada para cumprir o requisito de implementar unha clase abstracta/interface da cal derivar elementos. `Plato` herda dela, implementando a herdanza obrigatoria.
- **Atributos Privados/Protexidos**: Substituín a maioría dos atributos previamente públicos por privados (`_` e `__`). Engadíronse métodos getters (ex: `get_nome()`) nas partes necesarias.
- **Dunder Methods**: Engadiuse `__init__` e `__str__` en practicamente todas as entidades para permitir unha doada instanciación e presentación do obxecto por pantalla.
- **Métodos de clase/estáticos**: 
  - Engadiuse `crear_dende_string(nome)$` como método de clase (`@classmethod`) en `Ingrediente` para poder inicializalo por defecto.
  - Engadiuse `validar_unidade(unidade)*` como método estático (`@staticmethod`) en `LinaIngrediente` para validar a cadea da unidade (l, g, kg).
