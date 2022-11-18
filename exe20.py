import random
n = str(input('valor: '))
n1 = str(input('valor: '))
n2 = str(input('valor: '))
n3 = str(input('valor: '))
namebank = [n,n1,n2,n3]
random.shuffle(namebank)
print(namebank)