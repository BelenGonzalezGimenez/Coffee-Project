
from abc import ABC, abstractmethod

class ListaPersonalizada(ABC):

    def __init__(self):
        self.lista = []

    def __iter__(self):
        self.index = 0  # Inicializar el índice en cada iteración
        return self

    def __next__(self):
        if self.index < len(self.lista):
            elemento = self.lista[self.index]
            self.index += 1
            return elemento
        else:
            raise StopIteration

        
    @abstractmethod
    def agregar_elemento(self, elemento):
        pass

    @abstractmethod
    def eliminar_elemento(self, elemento):
        pass

    @abstractmethod
    def mostrar_elementos(self):
        pass

