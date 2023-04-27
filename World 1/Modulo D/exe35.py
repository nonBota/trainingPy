n  = float(input('digite o 1 segmento? '))
n1 = float(input('digite o 2 segmento? '))
n2 = float(input('digite o 3 segmento? '))

if n < n1 + n2 and n1 < n + n2 and n2 < n + n1:
    print('ele e um triangulo')
else:
    print('ele não e um triangulo ')