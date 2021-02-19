> Framework [Django 3.1](https://docs.djangoproject.com/en/3.1/)

## Documentación

* [Requisitos](#requisitos)
* [Estructura del Proyecto](#estructura-del-proyecto)
* [Instalación](#instalacion)
* [Instrucciones](#instrucciones)
* [Variables de entorno](#variables-de-entorno)
* [Lenguajes de traduccion](#Compile-message-languaje) 

## Librerias

* argon2-cffi==20.1.0
* asgiref==3.2.10
* boto3==1.15.18
* botocore==1.18.18
* cffi==1.14.3
* Django==3.1.2
* django-cors-headers==3.5.0
* django-environ==0.4.5
* django-filter==2.4.0
* django-storages==1.10.1
* djangorestframework==3.12.1
* djangorestframework-simplejwt==4.4.0
* jmespath==0.10.0
* Pillow==8.0.0
* psycopg2==2.8.5
* psycopg2-binary==2.8.6
* pycparser==2.20
* PyJWT==1.7.1
* python-dateutil==2.8.1
* pytz==2020.1
* s3transfer==0.3.3
* six==1.15.0
* sqlparse==0.4.1
* urllib3==1.25.10
* xlrd==1.2.0


## Requisitos

- virtualenv
- Python 3
- pip
- (PostgreSQL) >= 11

## Estructura del proyecto
> Esta es la estructura básica del boilerplate.

```
boilerplate/
    apps/
        users/
        ... more apps add here
    common/
        enums.py
        exeption_handler.py
    locale/
        es_MX/
            /LC_MESSAGES
                django.po
        ..... more languajes

    project/
        templates/
            default_urlconf.html
        urls.py
        wsgi.py
        settings.py
    .env.sample
    manage.py
    requeriments.txt

```
## Instalación
> Se deben instalar los requisitos mencionados anteriormente.
> En caso que la instalación de los paquetes falle, tomarse en cuenta el siguiente paquete

```
Ubuntu
sudo apt-get install libpq-dev python-dev
pip install setuptools

```

```
# Descargar o Clonar
....
```

## Deploy Local
#### Maquina virtual o localhost
> Las configuraciones pueden variar dependiendo del sistema operativo



## Variables de entorno
```
DEBUG=True
APPNAME=E-Learning
SECRET_KEY=DwmSyemSVo5afAnAovEon8nQtSJIb00MeDeKbpffVqo=
TIME_ZONE=UTC


DB_ENGINE='django.db.backends.postgresql'
DB_HOST=localhost
DB_NAME=**DATABASE NAME LOCAL**
DB_USER=**DATABASE USER LOCAL**
DB_PASSWORD=**DB PASSWORD LOCAL**
DB_PORT=5432



```

#### instrucciones
```

# Instalar entorno virtual 
$ python3 -m virtualenv venv

# Activar entorno virtual 
$ source venv/bin/activate

# Crear una copia de .env.sample
$ cp .env.sample .env

# modificar el .env con las variables de la base de datos local

# Instalar requerimientos
$ pip install -r requeriments.txt

# Ejecutar migraciones
$ python manage.py migrate

# Crear superususario
$ python manage.py createsuperuser

# Ejecutar archivos estaticos
$ python manage.py collectstatics

# Ejecutar proyecto
$ python manage.py runserver 0.0.0.0:8000


```


## Compile message languaje
```
# crear el archivo de mensajes 
$ python manage.py makemessages -l 'es_MX' -i venv

# subir el archivo al proyecto
$ django-admin compilemessages --locale es_MX
```