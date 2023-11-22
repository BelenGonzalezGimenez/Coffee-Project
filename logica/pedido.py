from ZODB import DB
import transaction
from persistent import Persistent

from iterable import ListaPersonalizada
'''Esta clase servira para instanciar cada pedido de los clientes. Sera una lista de productos
Atributos
    Heredados
        lista
    Propios
        index
        estado'''
class Pedido(ListaPersonalizada, Persistent):
    def __init__(self):
        super().__init__()
        self.index
        self.estado = 'en preparacion'

    ''' recibe un parametro producto, y lo agrega al final de la listaDeProductos'''
    def agregar_elemento(self, producto):
        self.lista.append(producto)

    '''recibe un parametro producto, y elimina 
    la primera ocurrencia del mismo'''
    def eliminar_elemento(self, producto):
        self.lista.remove(producto)

    '''Devuelve la lista de los productos que se ofertan en la cafeteria'''
    def mostrar_lista_de_productos(self):
        return self.lista

    '''Calcula la suma de los precios de todos los productos que estan en la lista que tiene por atributo'''
    def calcular_precio_del_pedido(self):
        # for producto in self.lista:
        #     precioTotal = producto.precio_unitario
        # return precioTotal
        #esto no esta hecho aun con el impuesto correspondiente

        #version con programacion funcional
        lista_precios = map(lambda producto: producto.precio, self.lista)
        return sum(lista_precios)

    @property
    def estado_del_pedido(self):
        return self.estado
    
    @estado_del_pedido.setter
    def estado_del_pedido(self, estado):
        self.estado_del_pedido = estado