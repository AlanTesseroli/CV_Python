while True:
    try:
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite um valor: '))
    except ValueError:
        print('Desculpe, você não digitou um numero')
    else:
        print(f'A soma dos dois números é: {num1+num2}')