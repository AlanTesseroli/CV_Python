while True:
    n = str(input('Digite a biblioteca: '))
    help(n)
    r = str(input('Gostaria de continuar [Digite "FIM" para encerrar]: '))
    if r not in 'fim':
        print('Vamos continuar')
    else:
        break