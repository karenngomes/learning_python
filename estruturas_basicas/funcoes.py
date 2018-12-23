def print_musica(nome):
    if nome == 'lh':
        print('O que te sobra alem das coisas casuais?')
    elif nome == 'cicero':
        print('E tudo foi desbotando, ate desaparecer')
    elif nome == 'wado':
        print('Vai doer, mas depois vai passar...')
    elif nome == 'rubel':
        print('Pinturas velhas nao renovam mais meu ar')
    else:
        print('Resto')

def print_duas_vezes(nome):
    print_musica(nome)
    print_musica(nome)

print_duas_vezes('cicero')
print_musica('lh')
print_musica('wado')
print_musica('mallu')
print_musica('rubel')
