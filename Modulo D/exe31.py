n = float(input('digite um valor: '))
if n <= 200:
    preco = n * 0.50
else:
    preco = n * 0.45
print('valor e {} '.format(preco))