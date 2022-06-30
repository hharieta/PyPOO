

import re


class Usuario:
    __edad = 0
    __nombre = ""
    def __init__(self) -> None:
        pass

    def saludar(self, saludo):
        print(saludo, self.nombre)
    
    # getter
    @property
    def edad(self):
        return self.__edad
    
    @property
    def nombre(self):
        return self.__nombre

    # setter
    @edad.setter
    def edad(self, valor):
        self.__edad = valor

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor


class Empleado(Usuario):
    # privado
    __salario = 0
    def modificar_salario(self, salario):
        self.__salario = salario
    
    def ver_salario(self):
        print(self.__salario)
    
    def saludar(self):
        super().saludar("Hola")
        print("Mi nombre es", self.nombre, "y gano", str(self.__salario))

# Objeto empleado instanciando la clase Empleado
empleado = Empleado()
empleado.nombre = "Gatovsky"
empleado.modificar_salario(1000)
empleado.edad = 27
print(empleado.edad, empleado.nombre)
empleado.saludar()