def fatorial (a, show=False):
    """"
              CALCULADORA DE FATORIAL
    -> a = valor para ser calculado
    -> para show (opcoinal) = mostra deselvolvimento do cálculo
    -> return = fatorial
    """
    f = 1
    for c in range(a, 0, -1):
        f *= c
    if show:
        for c in range(a, 0, -1):
            if c > 1:
                print(f'{c} x ',end='')
            else:
                print(f'{c} = ',end='')
    return f


a = int(input('Digite um valor: '))
print(fatorial(5,show=True))