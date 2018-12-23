x = int(input())
if x < 10:
    tamanho = 'menor que 10'
elif x <= 100:
    tamanho = 'entre 10 e 100'
else:
    tamanho = 'maior que 100'

print(tamanho)

nMax = 6
n = 1
a = []

while(n < nMax):
    a.append(1.0/n)
    n += 1

print(a)

lista = ['Karen', 'Nich', 'Brubs', 'Lore', 'Pedro']
nome = input('Digite um nome: ')
for i in range(len(lista)):
    if lista[i] == nome:
        print('O nome %s esta na lista' %nome)
else:
    print('O nome %s nao esta na lista' %nome)

y = input('Digite um numero: ')
print(y,type(y))
z = eval(y)
print(z, type(z))