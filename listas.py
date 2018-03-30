progs = ['Pink Floyd', 'Genesis', 'Yes']

for prog in progs:
    print(prog)

#Troca o ultimo elemento
progs[-1] = 'King Crimson'

progs.append('Camel')
progs.remove('Genesis')

print(progs)

#Ordenar a lista
progs.sort()
#Inverter a lista
progs.reverse()

print(progs)

lista = ['A','B', 'C', 'D', 'E']
print('Lista:', lista)

while lista:
    #fila
    print('Saiu', lista.pop(0),'faltam', len(lista))

lista += ['F', 'G', 'H']

while lista:
    #pilha
    print('Saiu', lista.pop(), 'faltam', len(lista))

a = [1.0, 2.0, 3.0]
a.append(4.0)
print(a)
a.insert(2,2.5)
print(a)

# copia por referencia
b = a
b[0] = 0.0
print('a:', a)
print('b:', b)

# copia independente

c = a[:]
c[0] = 5.0
print('a:', a)
print('c:', c)

# matrizes

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matriz[1])
print(matriz[2][2])

