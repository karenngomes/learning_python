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