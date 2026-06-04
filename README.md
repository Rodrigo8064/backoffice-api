# Backoffice

Plataforma interna para gestão de atributos de produtos e backoffice de categorização de e-commerce. Desenvolvida em Django-Ninja.

---

## Módulos

### AtributoHub
Cadastro e consulta de atributos de produtos para as fontes Shopify e Magalu. Permite vincular atributos a múltiplas fontes e famílias de produto simultaneamente.

### Backoffice
Gestão de categorias e tipos de produto.

---

## Stack

- **Python 3.13** + **Django 6.0**
- **PostgreSQL 17** (produção) / **SQLite** (desenvolvimento)
- **Gunicorn** como servidor WSGI
- **Whitenoise** para arquivos estáticos
- **MPTT** para hierarquia de categorias e tipos de produto
- **Select2** para campos de seleção com busca
- **Docker** + **Docker Compose** para containerização
- **Poetry** para gerenciamento de dependências

---

## Requisitos

- Docker e Docker Compose instalados
- Python 3.13+ (para desenvolvimento local)
- Poetry (para desenvolvimento local)

---

## Configuração

### Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# Ambiente
DEBUG=True
SECRET_KEY=sua-chave-secreta-aqui
ALLOWED_HOSTS=localhost,127.0.0.1

# Banco de dados (usado apenas com DEBUG=False)
POSTGRES_DB=backoffice
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=backoffice_db
POSTGRES_PORT=5432
```

> ⚠️ O arquivo `.env` nunca deve ser commitado no repositório.

---

## Rodando localmente

### Com Docker (recomendado)

```bash
# Subir todos os serviços
docker compose up --build

# Acessar em
http://localhost:8000
```

### Sem Docker

```bash
# Instalar dependências
poetry install

# Rodar migrations (usa SQLite com DEBUG=True)
poetry run python manage.py migrate

# Criar superusuário
poetry run python manage.py createsuperuser

# Subir servidor
poetry run python manage.py runserver
```

---

## Estrutura do projeto

```
├── core/                   # Configurações do projeto (settings, urls, wsgi)
├── attributes/             # App AtributoHub — atributos de produto
├── category/               # App categorias e fontes/famílias
├── product_type/           # App tipos de produto (hierarquia MPTT)
├── entrypoint.sh           # Script de inicialização para produção
├── Dockerfile
├── docker-compose.yaml
└── pyproject.toml
```

---

## Importação de atributos via CSV

O projeto inclui um management command para importar atributos em massa a partir de um arquivo CSV.

### Formato do CSV

```csv
name,expected_value,sources,families
cor,Azul,Shopify|Magalu,Casa e Jardim|Vestuário
tamanho,G,Shopify,Vestuário
voltagem,,Magalu,Eletrodomésticos
```

- Separador de colunas: `,`
- Separador de múltiplos valores: `|`
- `expected_value` é opcional
- `sources` e `families` devem estar cadastrados no banco via admin

### Uso

```bash
# Validar sem salvar (recomendado antes da importação real)
python manage.py import_attributes arquivo.csv --dry-run

# Importar
python manage.py import_attributes arquivo.csv

# Importar vinculando a um usuário específico
python manage.py import_attributes arquivo.csv --user admin
```

O comando é **idempotente** — pode ser executado múltiplas vezes sem duplicar dados.

---

## Admin

Acesse `/admin/` com um superusuário para gerenciar:

- Fontes e famílias de atributos
- Categorias e tipos de produto
- Usuários e permissões

---

## Acesso

| Rota | Descrição |
|---|---|
| `/attribute/` | Lista de atributos |
| `/categories/` | Lista de categorias |
| `/products/` | Lista de tipos de produto |
| `/admin/` | Painel administrativo |
