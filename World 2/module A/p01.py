nome = str(input('Qual eo seu nome?'))

if nome == 'lobo':
    print('executado if')
elif nome == 'pedro': 
    print('executado else if')
elif nome in 'ana claudia sara':
    print('executado else if')
else:
    print('executado else {}'.format(nome))