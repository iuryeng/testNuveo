[![Build Status](https://travis-ci.com/iuryeng/testNuveo.svg?branch=main)](https://travis-ci.com/iuryeng/testNuveo)

[![Coverage Status](https://coveralls.io/repos/github/iuryeng/testNuveo/badge.svg?branch=main)](https://coveralls.io/github/iuryeng/testNuveo?branch=main)

#  REST API Workflow (Desafio Nuveo)

Esta API foi construida como uma resolução do desafio de backend da Nuveo <br />
Você pode ver o desafio aqui: [Backend Test - N1](https://github.com/iuryeng/testNuveo/blob/main/Desafio%20N1%20-%20Integra%C3%A7%C3%A3o.pdf)<br />

Abra o terminal e clone minha resolução para um diretório de sua escolha com o comando: <br /> 
`$ git clone https://github.com/iuryeng/testNuveo.git`


                  
## Definindo um workflow

|Nomw|Tipo|Descrição|
|-|-|-|
|UUID|UUID|Identificador único do workflow|
|status|Enum(inserted, consumed)|Status do workflow|
|data|JSONB|Entrada de dados do workflow|
|steps|Array|Nome dos passos do workflow|

## Endpoints

|HTTP|URL|Descrição|
|-|-|-|
|POST|/workflow|Insira um workflow no banco de dados e na fila e a resposta desse endpoint é o próprio workflow enviado|
|PATCH|/workflow/{UUID}|Atualizar o status de um workflow específico|
|GET|/workflow|lista todos os workflows|
|GET|/workflow/consume|Consume um workflow da fila e gera um CSV do workflow.Data|

<br />

###  Tecnologias utilizadas
    1. Python: Django
    2. Python: Restframework
    3. Docker
    4. PostgreSQL
    5. RabittMQ



### Requisitos para rodar a API
    
    1. Python 3.8.5
    2. pip 21.1.1 
    3. Docker version 20.10.6
    4. docker-compose version 1.29.2
    5. postgres version 12.6
    



## Rode a app em um ambiente virtual local
 
___1. Entre no diretório /testNuveo___
  
>Crie uma virtual env: <br />`$ python3 -m venv venv`
        
>Instale as dependencias necessárias:<br /> `$ pip3 install requeriments.txt´ 
>Crie uma base de dados de workflow no postgres:<br />   

    
___2. Entre no diretório /testNuveo/apiworkflow/settings.py e defina o host da seguinte forma___ <br /> 
    
    DATABASES = {
    "default": {
        """
        "HOST": "localhost",
        
        """
    }
     
___3. Contrua as tabelas de workflow no banco de dados___:

>Contrua as migrations de workflow:<br /> 
`$ python3 manage.py makemigrations workflow`

>Faça as migrações necessarias: <br /> 
`$ python3 manage.py migrate`
    
>Rode a API:<br /> 
`$ python3 manage.py runserver`
    
>Acesse a API: http://localhost:8000/workflow      
                 
## Rode a app em um container do Docker

    
___1. Entre no diretório /testNuveo/apiworkflow/settings.py e defina o host da seguinte forma___ <br /> 
    
    DATABASES = {
    "default": {
        """
        "HOST": "db",
        
        """
    }
    
___2. Entre no diretório /testNuveo___

>starte o microserviço com o docker: <br /> 
 `$ sudo docker-compose up`


___3. Contrua as tabelas de workflow no banco de dados___

>Execute o shell do servico backend que está rodando no docker:
`$ sudo docker-compose exec backend sh`

>Contrua as migrations de workflow:<br /> 
`# python3 manage.py makemigrations workflow`

>Faça as migrações necessarias: <br /> 
`# python3 manage.py migrate`
    
>Acesse a API: http://localhost:8000/workflow

## Sistema de mensageria com rabbitMQ

___1. Entre no diretório /testNuveo/consumer.py___

Configure a url_parms com a url do seu AMQP URL: <br /> 
    
    url_params = pika.URLParameters('sua AMQP URL')

___2. Entre no diretório /testNuveo___

>Inicie o serviço de mensageria:<br />
`$ python3 consumer.py`

__.3 Iniciando o serviço em um container docker
`$ sudo docker-compose exec backend python3 consume.py`

   
## Exemplos de Uso
Se por algum acaso você tiver uma conta no postman, você pode acessar os exemplos de uso apertando nesse botão: [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/c7ffe1cd92832b3b40e1)

Você também pode acessar direto no seu browser preferido: <br />
1. com método get para listar todos os workflow: http://localhost:8000/workflow <br />
2. com o método post para criar workflows: http://localhost:8000/workflow <br />
3. com o método patch para corrigir workflows: http://localhost:8000/workflow/{UUID} <br />
4. com o método get para consumir um workflows e gerar o csv: http://localhost:8000/workflow/{UUID} <br />

Outra alternativa pode ser abrir o terminal e escrever os comandos listados abaixo para criar uma workflow, listar todos os workflows, corrigir um workflow ou consumir workflow gerando CSV


## Crie um Workflow

## Request

`POST /workflow/`   
     {        
        "status": "inserted",
        "data": {
            "name": "workflow-1",
            "work": "work-1",
            "score": 100,
            "tag_work": "@tagwork-1"
        },
        "steps": [
            "step-1",
            "step-2"
        ]
    }
### Response

    HTTP/1.1 201 Created
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Location: /thing/1
    Content-Length: 36

     ´{
        "UUID": "9464ed37-8b24-41f1-ab79-52f91716cc62",
        "status": "False",
        "data": {
            "name": "workflow-1",
            "work": "work-1",
            "score": 100,
            "tag_work": "@tagwork-1"
        },
        "steps": [
            "step-1",
            "step-2"
        ]
    }´

## Liste todos os workflows

### Request

`GET /workflow/`

     
     
### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

     ´{
        "UUID": "9464ed37-8b24-41f1-ab79-52f91716cc62",
        "status": "False",
        "data": {
            "name": "workflow-1",
            "work": "work-1",
            "score": 100,
            "tag_work": "@tagwork-1"
        },
        "steps": [
            "step-1",
            "step-2"
        ]
    }´


## Corrija um workflow

### Request

`PATCH /workflow/{UUID}`

{ "status": "consumed"}

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2
    
## Consumir workflow e gerar CSV

### Request

`GET /workflow/consume/{UUID}`

  

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2
