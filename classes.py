class MinhaClasse:
    "Primeira classe"
    i = 100
    counter = 0
    def hello():
        return 'Hello, world!'
    def f(x):
        return 'Ola, ' + x +'!'

class NumerosComplexos:
    "Classe que separa a parte real da imaginaria"
    def __init__(self, parteReal, parteImag):
        self.r = parteReal
        self.i = parteImag

class ClasseLista:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)

    def printlista(self):
        print(self.data)

x = MinhaClasse
# nao usa o () pois classe MinhaClasse nao tem __init__
print(x.__doc__)
print(x.hello())

print(x.f('Karen'))

numero = NumerosComplexos(3,-4.5)

print(numero.__doc__)
print('Parte real:', numero.r)
print('Parte imaginaria:', numero.i)

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

lista = ClasseLista()
lista.add(3)
lista.addtwice(40)
lista.add(20)
lista.printlista()