from ZODB import DB
import ZODB, ZODB.FileStorage
from transaction import commit

class Conexion:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo #nombre del modulo python
        self.storage = ZODB.FileStorage.FileStorage(nombre_archivo) #ruta del archivo que sera file storage
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root()

    def cerrar_conexion(self):
        self.connection.close()

    def commit(self):
        commit()

    def almacenar_objeto(self, nombre, objeto):
        self.root[nombre] = objeto
        self.commit()

    def recuperar_objeto(self, nombre):
        return self.root.get(nombre, None)

    def eliminar_objeto(self, nombre):
        if nombre in self.root:
            del self.root[nombre]
            self.commit()

    def listar_objetos(self):
        return list(self.root.keys())

    # Puedes agregar más métodos según tus necesidades
