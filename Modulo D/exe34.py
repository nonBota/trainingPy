money = float(input('salario? '))
if money <= 1.200:
    novo = money + (money * 15 / 100)
else:
    novo = money + (money * 10 / 100)

print('seu salario e {}'.format(novo))