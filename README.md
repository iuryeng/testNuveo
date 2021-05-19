#  REST API Workflow (Desafio Nuveo)

Esta API foi construida como uma resolução do desafio de backend da Nuveo <br />
Você pode ver o desafio aqui: [Backend Test - N1](https://github.com/iuryeng/testNuveo/blob/main/Desafio%20N1%20-%20Integra%C3%A7%C3%A3o.pdf)<br />

Abra seu terminal e clone minha resolução para um diretório de sua escolha com o comando: <br /> 
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

>inicie o serviço de mensageria:<br />
`$ python3 consumer.py`

   
## Exemplos de Uso


## Crie um Workflow

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
