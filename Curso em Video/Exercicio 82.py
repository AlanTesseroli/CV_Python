lista = []
par = []
impar = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)
    else:
        print('Esse número está repetido, logo, não será adicionado')
    r1 = str(input('Gostaria de continuar [S/N]: ')).upper()
    if r1 not in 'N':
        print('Certo, vamos continuar!')
    else:
        break
print(f'Os numeros digitados, foram: {lista}')
print(f'Os numeros pares digitados foram: {par}')
print(f'Os numeros impares digitados foram: {impar}')