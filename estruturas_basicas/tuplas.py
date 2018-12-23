#parecido com as listas, mas imutaveis
#parenteses são opcionais
#nao e possivel aplicar operacoes em tuplas
t1 = 0,1,2
print(t1)
lista = [10,11,12]

#converter lista para tupla
tupla = tuple(lista)
print(tupla)
#converter tupla para lista
lista = list(tupla)
print(lista)

#conjuntos
s1 = set(range(3))
s2 = set(range(10,7,-1))
s3 = set(range(2,10,2))

print('s1:', s1,'\ns2:',s2,'\ns3:',s3)

#união
s1s2 = s1.union(s2)
print('União de s1 com s2', s1s2)

#diferença
print('Diferença de s1s2 com s3:', s1s2.difference(s3))

#interseção
print('Interseção entre:', s1s2.intersection(s3))

#dicionario <nome> = {<elemento imutavel>:<objeto qualquer>}

dic = {'nome': 'Karen', 'sobrenome': 'Gomes'}
print(dic['nome'])
#adicionando elementos
dic['email'] = 'kngs@ic.ufal.br'

#apagar elemento
del dic['sobrenome']

print(dic)

#operadores booleanos
#all(): retorna True quando todos são verdadeiros
#any():retorno True quando algum for

print(0 and 3) #mostra 0
print(0 or 3) #mostra 3
print(2 and 3) #mostra 3
print(2 or 3) #mostra 2
print(not 0) #mostra True
print(not 2) #mostra False
print(2 in (2,3)) #mostra True
print(2 is 3) #mostra False