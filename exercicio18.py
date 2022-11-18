import math
n = float(input('Valor: '))
r = math.cos(math.radians(n))
r1 = math.sin(math.radians(n))
r2 = math.tan(math.radians(n))
print('result: {:.2f}, {:.2f}, {:.2f}'.format(r, r1, r2))