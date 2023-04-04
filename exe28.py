from random import randint 
from time import sleep
com = randint(0, 5)
eu = int(input('digite um numero: '))
print('processando')
sleep(3)
if com == eu:
    print('voce acertou ')
else:
    print('voce errou ')