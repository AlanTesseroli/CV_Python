def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
            valor = int(n)
            break
        except (ValueError):
            print('Erro de valor')
        except (TypeError):
            print('Erro de tipo')
    return valor


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
            valor = float(n)
            return valor
            break
        except (ValueError):
            print('Erro de valor')
        except (TypeError):
            print('Erro de tipo')
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar esse valor')
            valor = 0
            return valor
            break



n = leiaint('Digite um inteiro: ')
p = leiafloat('Digite um real:')
print(f'O valor inteiro digitado foi {n} e o real foi {p}')