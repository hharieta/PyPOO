from abc import ABC, abstractmethod

## Clases abstractas ##

# 1er nivel de abstracción
class EstructuraAbstracta(ABC):
    @abstractmethod
    def obtener():
        pass

    @abstractmethod
    def agregar():
        pass


# 2o nivel de abstracción
class Hash(EstructuraAbstracta):
    datos = dict()

    def obtener(self, llave):
        self.datos[llave]
    
    def agregar(self, llave, valor):
        self.datos[llave] = valor


# 3er nivel de abstracción
class FilaBanco:
    def __init__(self, almacen_usuarios) -> None:
        if not isinstance(almacen_usuarios, EstructuraAbstracta):
            raise ValueError('Store is not supported')

        self.usuarios = almacen_usuarios

    def siguiente(self, numero):
        return self.usuarios.obtener(numero)
    
    def fomar(self, numero, usuario):
        self.usuarios.agregar(numero, usuario)
    

# instancia
FilaBanco(Hash())
