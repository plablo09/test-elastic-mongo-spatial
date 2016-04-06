# test-elastic-mongo-spatial
Pruebas de búsquedas geoespaciales usando elasticsearch y mongodb


Basado en [este](https://github.com/soldotno/elastic-mongo) repositorio y adaptado para búsquedas espaciales.


### Instalación

Todo está basado en contenedores de [Docker](https://www.docker.com/), entonces la instalación es relativamente fácil. En lo siguiente voy a suponer que vamos a instalar todo en Ubuntu 14.04

La idea es más o menos esta:

* Vamos a usar 3 imágenes de Docker para los 3 contenedores de la base de datos, configurada como replicaSet
* Una imágen para el transporter, que se encarga de sincronizar entre mongo y elasticsearch
* Una imagen para el contenedor de elasticsearch.

La configuración de todo esto está en el archivo `docker-compose.yml`


### Linux
Instalar Docker de acuerdo a [estas](https://docs.docker.com/engine/installation/linux/ubuntulinux/) instrucciones

Instalar docker-composer, la forma más sencilla es instalarlo directamete de pip:

    $ pip install docker composer

**Nota:** si instalas el composer de esta forma es importante utilizar un _virtualenv_. Al parecer docker-composer utiliza algunas librerías de python indispensables para apt, entonces puede haber conflicto y descomponer todo. [Aquí](http://exponential.io/blog/2015/02/10/install-virtualenv-and-virtualenvwrapper-on-ubuntu/) están las instrucciones para instalar virtualenv.

Una vez instalado Docker y docker-composer:

    git clone https://github.com/plablo09/test-elastic-mongo-spatial.git
    cd test-elastic-mongo-spatial
    docker-compose up -d

Con esto quedan levantados los tres servicios (mongodb, elasticsearch y el transporter). Lo puedes ver con `docker ps`:

    $ docker ps

    CONTAINER ID        IMAGE                              COMMAND                  CREATED             STATUS              PORTS                                                NAMES
    66b26b049a4d        golang:1.5                         "/transporter/run.sh"    4 minutes ago       Up 4 minutes                                                             elasticmongo_transporter_1
    a6a3955dd6f1        stabenfeldt/elasticsearch-marvel   "/docker-entrypoint.s"   7 minutes ago       Up 7 minutes        0.0.0.0:9200->9200/tcp, 0.0.0.0:9300->9300/tcp       elasticmongo_elasticsearch_1
    55c162aaed7c        mongo:3.0.6                        "/usr/bin/mongod --re"   10 minutes ago      Up 10 minutes       0.0.0.0:27017->27017/tcp, 0.0.0.0:28017->28017/tcp   elasticmongo_mongo1_1
    8ce90de2b00c        mongo:3.0.6                        "/usr/bin/mongod --re"   10 minutes ago      Up 10 minutes       0.0.0.0:27018->27017/tcp, 0.0.0.0:28018->28017/tcp   elasticmongo_mongo3_1
    9a7d6aade048        mongo:3.0.6                        "/usr/bin/mongod --re"   10 minutes ago      Up 10 minutes       0.0.0.0:27019->27017/tcp, 0.0.0.0:28019->28017/tcp   elasticmongo_mongo2_1



Para conectarte a una instancia de mongo (esto abre una terminal en el _container_):

    docker exec -i -t elasticmongo_mongo1_1  bash

Desde el host:

    mongo localhost:27017

**Nota:** para esto último necesitas tener instalado mongo-tools (la versión 3.06).
[Aquí](https://docs.mongodb.org/v3.0/tutorial/install-mongodb-on-ubuntu/) están las instrucciones.

Para buscar en elasticsearch (desde el host):

    curl -XGET "http://localhost:9200/harvester-test/_search?pretty&q=*:*"

**Nota:** Por lo pronto la base de datos tiene una única entrada. Estoy trabajando en subir unos datos más sustantivos

Para de6tener todos los containers (o sea, todos los servicios):

     docker-compose stop
