# INSTRUCCIONES PARA COMENZAR UN PROYECTO CON DJANGO

## Instalación
Para instalar Django necesitamos el siguiente comando:
```
python -m pip install Django
```

Ahora necesitan crear una carpeta donde van a tener su proyecto de Django.

En este caso yo voy a utilizar 'Clase9-Django', luego ubican su consola en esa carpeta para ejecutar el siguiente comando:

```
django-admin startporoject <Nombre sin espacios> .

ej: django-admin startproject SitioEjemplo .
```

## Despliegue

Cuando ya lo tengan, pueden Desplegar su sitio con el siguiente comando:

```
python manage.py runserver 0.0.0.0:8000
```

Van a su navegador y escriban en el buscador:
``` 
localhost:8000
```

## Creando un nuevo apartado

Ahora que tenemos esta parte hecha, debemos hacer un apartado donde tengamos nuestros distintos "servicios" o "aplicaciones".
Piensen que si dividen su página en ventanas, cada servicio/aplicacion es un conjunto de ventanas que se dedicarán a un bloque de su programa.

Para crear nuestro apartado utilizamos el siguiente comando:
```
python manage.py startapp <nombre sin espacios>

ej: python manage.py startapp Curriculum
```

Luego, vamos a tener las siguientes carpetas y archivos:
```
Curriculum/
    migrations/
    __init__.py
    admin.py
    apps.py
    models.py
    test.py
    views.py
```
Y debemos crear uno nuevo llamado "urls.py"
```
Curriculum/
    migrations/
    __init__.py
    admin.py
    apps.py
    models.py
    test.py
    urls.py
    views.py
```

Ahora vamos al urls que se encuentra en SitioEjemplo/urls.py
y agregamos la siguiente línea:
``` py
path('cv/', include('Curriculum.urls'))
```

Luego en nuestro "Curriculum.urls.py" vamos a añadir el siguiente contenido:
``` py
from django.urls import path
from . import views

urlpatterns = []
```

En este espacio nosotros podemos tener las direcciones para las distintas páginas según necesitemos.

## Creando una nueva vista html

Creamos una carpeta llamada templates en "Curriculum/".

En esta carpeta vamos a meter nuestros archivos html.

Agregamos en "Curriculum/templates/" los archivos html que querramos.

Y luego debemos dirigirnos hacia la "Curriculum/views.py".

Agregamos las siguientes líneas para que nos cargue nuestra página:

``` py
def PrimeraPagina(request):
    return render(request, 'PaginaEjemplo/pagina.html', {})
```

Ahora debemos ir hacia Curriculum/urls.py y agregamos la ruta para que se pueda acceder a nuestra "view" que acabamos de crear.

Para ello, en el espacio de urlpatterns=[], y vamos a meter en la lista la siguiente línea:
``` py
path('Ejemplo1/', views.PrimeraPagina, name="PrimeraPagina"),
```

Ahora podríamos volver a cargar nuestra página y nos va a aparecer un error.
Eso es porque nos falta agregar a nuestra configuración el apartado "Curriculum" que creamos. 

Para ello nos dirigimos al archivo "SitioEjemplo/settings.py" y ubicamos lista llamada "INSTALLED_APPS", en esta lista apareceran varios elementos, ya hora debemos agregarle uno nuevo.
 
En este caso le agregaremos lo siguiente:
``` py
'Curriculum.apps.CurriculumConfig'
```

En este caso lo que estamos diciendo es que vaya a "Curriculum/apps.py" y obtenga la función o elemento "CurriculumConfig".

Ahora si la página debe funcionar.

## Utilizando la vista HTML con CSS
Ahora para que podamos utilizar el CSS, debemos agregar una nueva carpeta llamada "static" en el apartado donde querramos utilizarlo. En este caso lo crearemos en "Curriculum/static/".

Ya aquí debemos colocar nuestros archivos .css donde tendremos los estilos que querramos utilizar en nuestras páginas html.

Para el ejemplo vamos a agregar las siguientes líneas al css:
``` css
.Cabeza {
    color:green;
}
.CabezaSecundaria {
    color:orange;
}
.EstiloCabeza {
    font-family: Arial, Helvetica, sans-serif;
}
```

Ahora debemos ir a nuestro HTML donde deseamos utilizar nuestro css y vamos a agregar al inicio del documento la siguiente línea:
```
{% load static %}
```

Y ahora en nuestro apartado "head", debemos agregar un nuevo elemento, ya no será "style", sino ahora será "link":
``` html
<head>
        <title>Pagina con css</title>
        <link rel="stylesheet" href="{% static 'estilo1.css' %}">
</head>
```