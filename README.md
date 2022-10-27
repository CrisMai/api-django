# api-django

#################################################################

Conta Virtual

Criar uma API que seja possível utilizar uma conta virtual tendo as seguintes funcionalidades:
Criar conta virtual;
Realizar débito;
Realizar crédito;
Exibir extrato.

Linguagem utilizada: Python

Preparando o ambiente
 
Ferramentas utilizadas:
Python 3.11.0
Django 4.1.2
Django Rest Framework
Postman

#################################################################

Comandos usados:
pip install django
pip3 install djangorestframework
pip install markdown

Criado ambiente virtual - Windows
 
Comando usado:
python -m venv ./venv

Ativação do ambiente virtual

Comando usado:
source venv/Scripts/activate

#################################################################

Iniciando projeto

Criado um projeto chamado apiDjango.
 
Comando usado:
django-admin startproject apiDjango .

Subindo server

Comando usado: 
python manage.py runserver 

#################################################################

Criado migrations conforme modelo de dados da aplicação

Comando usado:
python manage.py makemigrations 

Subir para o banco de dados os modelos criados anteriormente

Comando usado:
python manage.py migrate

#################################################################

End points criados:

# Recuperar contas
Get  http://localhost:8000/api/v1/contas/

# Criando uma conta
Post http://localhost:8000/api/v1/contas/conta
Parâmetros passado no body, JSON:
{
    "nome": "Conta A",
    "valor": 200,
    "descricao": "Criando nova conta"
}

# Realizando crédito em uma conta
Post http://localhost:8000/api/v1/contas/credito
Parâmetros passado no body, JSON:
{
    "conta": "Conta A",
    "valor": 200,
    "descricao": "Depósito em conta",
    "tipo_transacao": "Credito"
}

# Realizando débito em uma conta
Post http://localhost:8000/api/v1/contas/debito
Parâmetros passado no body, JSON:
{
    "conta": "Conta A",
    "valor": -250,
    "descricao": "Saque da conta",
    "tipo_transacao": "Debito"
}

# Recuperando extrato total
Get http://localhost:8000/api/v1/contas/extratoAll

# Recuperando extrato filtrando por "crédito" ou "débito"
Get http://localhost:8000/api/v1/contas/extrato/<query>
