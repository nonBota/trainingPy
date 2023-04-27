from datetime import date
n = int(input('ano? '))
if n == 0:
    n = date.today().year
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('o ano e bissexto')
else:
    print('o ano não e bissexto')
