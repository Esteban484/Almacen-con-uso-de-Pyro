import sys
#importacion de la clase persona 
from persona import persona

#Importacion de librerias para utilizar pyro
import Pyro4
import Pyro4.util

#importar la clase almacenes  
from almacen import almacenes

sys.excepthook=Pyro4.util.excepthook

#ubicacion del objeto del almacén 
almacenes = Pyro4.Proxy("PYRONAME:ejemplo.almacen")

#Llamada de los metodos del almacen para poder visualizar el menu
janet = persona("Janet")
henry = persona("Henry")
janet.visit(almacenes)
henry.visit(almacenes)