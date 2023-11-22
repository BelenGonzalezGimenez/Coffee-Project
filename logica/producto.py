#base de datos
from ZODB import DB
import transaction
from persistent import Persistent
#utiles
from time import time
from utiles import Util

'''La clase producto se utilizara para instaciar objetos del tipo Producto
Sus atributos son:
    datos[  'descripcion':' ',
            'precio': 0,
            'cantidad': 0,
            'fechaCreacion': None,
            'fechaModificacion': None]
Getters y Setters:
descripcion()
precio()
cantidad()
fechaModificacion()

Metodos de instancia
    Publicos:    
        *info_del_producto()
        *vender()
'''
class Producto(Persistent):
    def __init__(self, nombre, precio, cantidad):
        self.datos = {
            'descripcion': nombre,
            'precio': precio,
            'cantidad': cantidad,
            'fechaCreacion': time(),
            'fechaModificacion': None
        }

    ''' Muestra la informacion del producto '''
    def info_del_producto(self):
        mensaje = f"Descripcion: {self.datos['descripcion']}" + "\n" + f"Precio: {self.datos['precio']}" + "\n" + f"Cantidad Disponible: {self.datos['cantidad']}"
        return mensaje

    ''' Realiza el calculo de la operacion venta, recibiendo como parametro la cantidad a vender '''
    def vender(self, cantidad):
        if Util.XmayorY(cantidad, 0) and Util.XmayorIgualY(self.datos['cantidad'], cantidad):
            self.datos['cantidad'] -= cantidad
            self.datos['fechaModificacion'] = time()
            return f"{cantidad} unidades vendidas. Actualizado: {self.datos['fechaModificacion']}"
        elif cantidad <= 0:
            return 'La cantidad a vender debe ser mayor que cero.'
        else:
            return 'No hay suficientes unidades disponibles.'

    @property
    def descripcion(self):
        return self.datos['descripcion']

    '''Setea la descripcion del producto, lanza una excepcion en caso de introducir tipo de dato distinto a str'''
    @descripcion.setter
    def descripcion(self, nueva_descripcion):
        try:
            #captura de la excepcion  
            if type(nueva_descripcion) != str:
                raise Exception('Tipo de dato Invalido')
        except Exception as e:
            #tratamiento de la excepcion
            mensaje = 'No se puede registrar ' + str(nueva_descripcion)
            return mensaje 
            #propagacion de la excepcion
            raise
        else:
            self.datos['descripcion'] = nueva_descripcion
            self.datos['fechaModificacion'] = time()

    @property
    def precio(self):
        return self.datos['precio']

    '''Setea el precio del producto, recibiento como parametro el nuevo precio. 
    Como mejora deberamos poder tener una variable en la que se pueda poner cual es el tope de precio minimo'''
    @precio.setter
    def precio(self, nuevo_precio):
        if Util.XmayorY(nuevo_precio, 0):
            self.datos['precio'] = nuevo_precio
            self.datos['fechaModificacion'] = time()
        else:
            return 'El precio debe ser mayor a cero'

    @property
    def cantidad(self):
        return self.datos['cantidad']

    '''Setea la cantidad, recibiendo como parametro una cantidad. De ser menor a cero, retorna un mensaje'''
    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        if Util.XmayorIgualY(nueva_cantidad,0):
            self.datos['cantidad'] = nueva_cantidad
            self.datos['fechaModificacion'] = time()
        else:
            return 'La cantidad debe ser mayor o igual a cero.'

