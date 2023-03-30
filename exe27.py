n = str(input('informe o seu nome: ')).strip()
nome = n.split()
n1 = nome[0]
n2 = nome[len(nome)-1]
print('muito prazer seu primeiro nome é {} e seu sobrenome é {}'.format(n1,n2))
