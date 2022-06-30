class Numero:
    valor = (int)

    def __init__(self, valor):
        self.valor = valor

    def comparar(self, numero):
        if numero.valor > self.valor:
            return numero.valor
        return self.valor


class Cadena:
    valor = str

    def __init__(self, valor):
        self.valor = valor
    
    def comparar(self, cadena):
        palabras = [cadena.valor, self.valor]
        palabras.sort()

        return palabras[0]


class Lista:
    valor = list()

    def __init__(self, valor):
        self.valor = valor

    def comparar(self, lista):
        if len(lista.valor) > len(self.valor):
            return lista.valor
        
        return self.valor


def retornarMayor(a, b):
    return a.comparar(b)


num1 = Numero(10)
num2 = Numero(3)
str1 = Cadena("Gatovsky")
str2 = Cadena("Alex")
lst1 = Lista([1,2,3])
lst2 = Lista([1,2,3,4])

print(retornarMayor(num1, num2))
print(retornarMayor(str1, str2))
print(retornarMayor(lst1, lst2))
    