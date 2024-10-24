## Requisitos

* [Uv](https://docs.astral.sh/uv/) para gerenciamento de pacotes.
* [Oracle instant-client](https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip) instalado e configurado as vars de ambiente.


## Iniciando projeto

Entre na pasta do projeto e no raiz instale as dependências com:

```console
$ uv sync
```

Ative o ambiente virtual com:

```console
$ source .venv/bin/activate
```

Crie o arquivo .secrets.toml na raiz da pasta:

```toml
[development]
oracle_cx_user="usuario"
oracle_cx_pwd="senha"
oracle_cx_dsn="localhost:1521/bd"
```
Configure a var de ambiente para `development`:
```
$ export API_FASTAPI_ENV=development
```

Execute o projeto

```console
$ uv run fastapi dev app/main.py
```

### Comandos utéis do UV

Adicionando uma nova dependência no projeto:

```console
$ uv add polars
```

Removendo uma dependência no projeto:

```console
$ uv remove polars
```

Adicionando uma nova dependência de desenvolvimento no projeto:

```console
$ uv add --dev mypy
```