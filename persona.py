from __future__ import print_function
import sys
import Pyro4


if sys.version_info < (3, 0):
    input = raw_input



class persona(object):
    def __init__(self, name):
        self.name = name
    #Metodo para la utilizacion del menu
    def visit(self, warehouse):
        while True:
        
            print ("\nSelecciona una opción")
            print ("\t1 - Agregar producto")
            print ("\t2 - Listar productos")
            print ("\t3 - Sacar producto")
            print ("\t4 - Salir \n")

            # solicituamos una opción al usuario
            opcionMenu = input("Inserta una opcion >> ")
            if opcionMenu=="1":
    
                #Ingresar objetos al almacen
                self.deposit(warehouse)

            elif opcionMenu=="2":
                #Lista de prodcutos ingresados
                print ("Listado de productos")
                print(warehouse.list_contents())
            

            elif opcionMenu=="3":
                #Retirar productos del almacen
                self.retrieve(warehouse)
            elif opcionMenu=="4":

                break

            else:

                print ("")

                input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
            
    #Metodo que se utiliza para ingresar una vatiable el cual sera el producto
    def deposit(self, warehouse):
        item = input("Ingrese el prodcuto que desee almacenar: ").strip()
        if item:
            warehouse.store(self.name, item)
    #Metodo para retirar un prodcito mediante el ingreso del nombre
    def retrieve(self, warehouse):

        item = input("Ingrese el producto que desea retirar: ").strip()
        if item:
            warehouse.take(self.name, item)
            
