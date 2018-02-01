import string

musicos = [('Page', 'guitarrista', 'Led Zeppelin'),
           ('Fripp', 'guitarrista', 'King Crimson')]

#Parametros identificados pelo ordem
msg = '{0} é {1} do {2}'

for nome, funcao, banda in musicos:
    print(msg.format(nome, funcao, banda))

#Parametros identificados pelo nome
msg = '{saudacao}, são {hora:02d}:{minuto:02d}'
print(msg.format(saudacao='Bom dia',hora = 7, minuto = 30))

# [inicio:fim+1:intervalo]
print('Python' [::-1])

#Cria uma string template
st = string.Template('$aviso aconteceu em $quando')

#Preenche o modelo com um dicionario
s = st.substitute({'aviso': 'Falta de eletricidade',
                   'quando':'01 de Fevereiro de 2018'})

print(s)
