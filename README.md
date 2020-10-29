# Juego Tiro Parabólico
Este trabajo consiste en un juego de tiro parabólico, donde el usuario usa un proyectil para destruir los objetivos. En general, es un juego de entretenimiento, que puede servir como una buena forma de pasar el tiempo o de mejorar las habilidades de programación de quienes lo usan.

El juego se puede ejecutar desde cualquier lugar donde se pueda instalar Python, sea en una computadora Windows, Mac OS o Linux. 

El código inicial para este juego fue recuperado de: http://www.grantjenks.com/docs/freegames/cannon.html

# Requisitos
Tener la version de Python 2.7 en adelante

# Instalación
Para poder utilizar este código es necesaria la instalación de las siguientes librerias de Python
```shell
from random import randrange, randint
from turtle import *
from freegames import vector.
```
Estas líneas de código son necesarias para correr correctamente el código.
Para mayor información sobre la librería Turtle puede consultar la página : https://docs.python.org/3/library/turtle.html

# Desarrollando
Puede crear una copia de este repositorio usando el comando de Git
```shell
git clone https://github.com/MajoDiaz/Tiro-Parabolico.git
```
Una vez creado la copia, puede porceder a trabajar sobre este repositorio creando su propia rama.

# Características del juego
* Lo primero que debe de aparecer al correr este código es una ventana de juego. En esta ventada, a la derecha, se empezarán a generar los objetivos. Al dar click dentro de la ventana, se lanza un proyectil en esa dirección. Este proyectil se mueve con una trayectoria de tiro parabólico.
* El objetivo de este juego es eliminar a todos los objetivos con el proyectil. Los objetivos seguirán apareciendo hasta que sean eliminados por completo.
* Se puede modificar la velocidad de los objetivos y del proyectil. Igualmente se puede cambiar el tamaño y color de ambos.

# Contribuciones
Si le gustaría contribuir, por favor haga un fork del repositorio y utilice una rama. Las solicitudes de pull son igualmente bienvenidas.
