#  REST API Workflow (Desafio Nuveo)

Esta API foi construida durante a resolução do desafio de backend da Nuveo 

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
        
>Instale as dependencias necessárias:<br /> `$ pip3 install -r requeriments.txt`

>Inicie o shell no postgres:<br /> `$ sudo -u postgres psql`
        
>Crie uma base de dados de workflow no postgres:<br />`$ createdb workflow`    


    
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
                 
## Rode a app no Docker

    
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
                  
## REST API - Defining a workflow

|Name|Type|Description|
|-|-|-|
|UUID|UUID|workflow unique identifier|
|status|Enum(inserted, consumed)|workflow status|
|data|JSONB|workflow input|
|steps|Array|name of workflow steps

## Endpoints

|Verb|URL|Description|
|-|-|-|
|POST|/workflow|insert a workflow on database and on queue and respond request with the inserted workflow|
|PATCH|/workflow/{UUID}|update status from specific workflow|
|GET|/workflow|list all workflows|
|GET|/workflow/consume|consume a workflow from queue and generate a CSV file with workflow.Data|

<br />

## Exemplos de Uso


## Create a new Thing

## Request

`POST /workflow/`

    curl -d '{"data": {{"name": "workflow-1","work": "work-1",{"tag_work": "@tagwork-1",score": 100},{"steps":"step-1","step-2"]}'-H "Content-Type: application/json" -X POST http://localhost:8000/wrokflow

### Response

    HTTP/1.1 201 Created
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Location: /thing/1
    Content-Length: 36

    {"id":1,"name":"Foo","status":"new"}

## Liste todos os workflows

### Request

`GET /workflow/`

    curl -i -H 'Accept: application/json' http://localhost:7000/thing/

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    []


