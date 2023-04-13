n = int(input('valor? '))
n1 = int(input('valor? '))
n2 = int(input('valor? '))
menor = n
maior = n
if n1 < n and n1 < n2:
    menor = n1
if n2 < n and n2 < n1:
    menor = n2

if n1 > n and n1 > n2:
    maior = n1
if n2 > n and n2 > n1:
    maior = n2

print('o valor menor e  {}'.format(menor))
print('o valor maior e {}'.format(maior))
