# Receitas con SQLite

Esta é a implementación da persistencia con SQLite baseada no deseño do punto de partida do proxecto `recetas`.

## Requisitos
- Python 3.x
- O módulo estandar `sqlite3` está incluído en Python, polo que non se necesitan dependencias adicionais.

## Como Executar
Podes probar o código executando directamente o script `main.py` desde este mesmo directorio:

```bash
python main.py
```

Isto creará na mesma carpeta un arquivo chamado `recetas.db`, cargará unhas receitas de proba na base de datos e recuperaraas amosándoas pola consola.

## Estrutura
- **modelos.py**: Contén as clases do dominio e o diagrama orixinal de `Plato`, `Ingrediente`, `LinaIngrediente`, `EntradaMenu`. Modelos actualizados para incluír os campos de ID para a súa xestión coa base de datos.
- **db_sqlite.py**: Implementa o modelo DAO (`RecetasDAO`) usando chamadas SQL puras a través do módulo `sqlite3`.
- **main.py**: Ficheiro con exemplos de uso.
