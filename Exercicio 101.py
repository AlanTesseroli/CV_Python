def voto(n):
    if (2022 - n) >= 16 and (2022 - n) < 18 or (2022 - n) >= 65:
        print(f' Com {2022-n} anos: VOTO OPCIONAL')
    if (2022 - n) >= 18 and (2022 - n) < 65:
        print(f' Com {2022-n} anos: VOTO OBRIGATÓRIO')
    if (2022 - n) < 16:
        print(f' Com {n} anos: VOTO NEGADO')


n = int(input('Digite seu ano de nascimento: '))
voto(n)