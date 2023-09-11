house = float(input('digite o valor da casa: '))
salary = float(input('digite o valor do seu salario: '))
years = int(input('em quantas parcelas: '))

prestacao = house / (years * 12 )
min = salary * 30 / 100
print('para pagar a casa de R${:.2f} em {} anos'.format(house, years), end='')
print('  a prestação sera de R${:.2f}'.format(prestacao))

if prestacao <= min:
    print('emprestimo concedido')
else:
    print('negado')