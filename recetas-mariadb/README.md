# Receitas con MariaDB

Esta é a implementación da persistencia con MariaDB / MySQL baseada no deseño principal de `recetas`.

## Requisitos
- Python 3.x
- Servidor de base de datos MariaDB ou MySQL en execución na túa máquina.
- Librería `pymysql`.

### Instalación de dependencias
Asegúrate de instalar a dependencia de conexión executando:

```bash
pip install pymysql
```

## Como Executar

Antes de executar, asegurate de que o teu servidor MariaDB está levantado.
No ficheiro `main.py`, a conexión á base de datos establécese cun usuario `root` sen contrasinal (`""`) por defecto en `localhost`. Podes modificar eses parámetros no chamamento a `RecetasMariaDBDAO(user='...', password='...')`.

Cando estea listo, executa:

```bash
python main.py
```

Isto creará automaticamente a base de datos `recetas_db` xunto a todas as súas táboas relacionais, inserirá os datos de proba e os recuperará para amosalos na terminal.

## Estrutura
- **modelos.py**: Contén as mesmas clases do dominio definidas previamente (sen dependencias ORM nin SQL).
- **db_mariadb.py**: Implementa o modelo DAO (`RecetasMariaDBDAO`) co uso de cursores `pymysql` para construír a base de datos e gardar ou recuperar a información.
- **main.py**: Ficheiro principal para probar o código.
