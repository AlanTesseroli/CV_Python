time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    tot = int(input(f'Digite quantas partidas {jogador["nome"]} jogou: '))
    partidas.clear()

    for c in range (0, tot):
        partidas.append(int(input(f'Quantos gols foram feitos na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        r = str(input('Gostaria de continuar [S/N]: ').upper())
        if r in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if r == 'N':
        break

print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()

for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*40)

while True:
    busca = int(input('Mostrar dados de qual jogador? '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe jogador com código {busca}')
    else:
        print(f' --  LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'     No jogo {i+1} fez {g} gols')
    print('-'*40)
print('Volte sempre')
