lista = []
while True:
    n1 = int(input('Digite um valor: '))
    if n1 not in lista:
        lista.append(n1)
    else:
        print('Esse número está repetido, logo, não será adicionado')
    r1 = str(input('Gostaria de continuar [S/N]: ')).upper()
    if r1 not in 'N':
        print('Certo, vamos continuar!')
    else:
        break
lista.sort(reverse=True)
print(lista)