from ZODB import DB
import transaction
from persistent import Persistent

#from producto import Producto
from iterable import ListaPersonalizada

'''La clase Menu_Restaurante es la plantilla con la que se van instanciar los objetos
que representan al Menu de la cafeteria.
Hereda de ListaPersonalizada.

Atributos:
    Heredados:
        lista[]
    Propios:
        index 

Tiene definidos los siguientes metodos:
Metodos de instancia:
    Redefinimos los siguientes metodos heredados:
        agregar_elemento()
        eliminar_elemento()
        mostrar_elementos()
    Metodos propios de la clase:
        tamanho_lista()
        
'''
class Menu(ListaPersonalizada, Persistent):

    def __init__(self):
        super().__init__()
        self.index = 0

    '''Recibe como parametro un elemento y lo agrega al final de la lista'''
    def agregar_elemento(self, elemento):
        self.lista.append(elemento)

    '''Rcibe como parametro un elemento, lo busca en la lista y si lo encuentra lo elimina
     de la lista. Devuelve un mensaje si no se encuentra el elemento'''
    def eliminar_elemento(self, elemento):
        if elemento in self.lista:
            self.lista.remove(elemento)
        else:
            return (f"{elemento} no se encuentra en la lista.")

    '''Devuelve la lista'''
    def mostrar_elementos(self): #aqui solo esta devolviendo el primer elemento
        #debo crear un iterable
        #return self.lista debe retornar esto en vez del codigo de abajo. El front debera gestionar como mostrar cada elemento de la lista
        #para prueba
        # for producto in self.lista:
        #print(producto.info_del_producto()) #16/10/2023 aqui esta el problema, el return hace que salga de la funcion y devuelve el control a la funcion invocadora
        return self.lista
    
    '''Devuelve el tamanho de la lista'''
    def tamanho_lista(self):
        return len(self.lista)
