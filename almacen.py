from __future__ import print_function
import Pyro4
@Pyro4.expose
@Pyro4.behavior(instance_mode="single")

#Creacion de la clase almacenes
class almacenes(object):
    #inicializacion del objeto
    def __init__(self):
        self.productos = ["bicicleta"]
    #Metodo para listar los prodcutos ingresados
    def list_contents(self):
        return self.productos
    #Metodo para tomar prodcutos
    def take(self, name, item):
        self.productos.remove(item)
        print("Se tomo el siguiente producto {1}.".format(name, item))
    #Metodo para alamcenar objetos
    def store(self, name, item):
        self.productos.append(item)
        print("Se guardo el siguiente producto {1}.".format(name, item))

#Inicializacion del servidor
def main():
    Pyro4.Daemon.serveSimple(
            {
                almacenes: "ejemplo.almacen",
                
            },
            ns = True)

if __name__=="__main__":
    main()
