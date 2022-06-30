
# clase padre
class Usuario:

    # método constructor
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self, saludo):
        print(saludo, self.nombre)


# clase hija (hereda todos los métodos y atributos de Usuario)
class Empleado(Usuario):
    salario = 0

    def set_salario(self, salario):
        self.salario = salario
    
    def get_salario(self):
        print(self.salario)
    
    # reescribir método de la clase padre
    def saludar(self):
        super().saludar("hola")
        print("Hola soy", self.nombre, "y gano", self.salario)


# instanciación de objetos
empleado = Empleado("Gatovsky")
empleado.set_salario(1000)
empleado.saludar()


class Pagina():
    def __init__(self, pie_pagina):
        self.pie_pagina = pie_pagina

    def Imprimir_pie_pagina(self):
        print(self.pie_pagina)


class PaginaLegal(Pagina):
    def Imprimir_pie_pagina(self):
        return super().Imprimir_pie_pagina()
    
html = PaginaLegal("<p>HOLA</p>")
html.Imprimir_pie_pagina()