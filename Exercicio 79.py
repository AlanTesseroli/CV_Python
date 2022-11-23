lista = list()
while True:
    n1 = int(input('Digite um valor: '))
    if n1 not in lista:
        lista.append(n1)
    else:
        print('Esse número já foi digitado, não irei adiciona-lo')
    r1 = str(input('Gostaria de continuar [S/N]:')).upper()
    if r1 not in 'N':
        print('Certo, vamos continuar')
    else:
        break
print(sorted(lista))