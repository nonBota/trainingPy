velocidade = float(input('qual e a sua velocidade?'))

if velocidade > 80:
                multa = (velocidade-80) * 7
                print('voce foi multado em {}'.format(multa))
else:
    print('você passou no radar parabens')