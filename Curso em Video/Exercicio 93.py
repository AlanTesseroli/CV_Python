fut = {}
gol = []
nome = {'nome': str(input('Digite o nome do jogador: '))}
fut.update(nome)
x = int(input('Quantas partidas eles jogou: '))
for c in range(0,x):
    gol.append(int(input(f'Quantos gols na partida {c+1}: ')))
gols = {'gols': gol}
fut.update(gols)
tot = {'total': sum(gol)}
fut.update(tot)
print('-=-'*30)
print(fut)
print('-=-'*30)
for c, i in fut.items():
    print(f'O campo {c} tem o valor {i}')
print('-=-'*30)
print(f'O jogador {fut["nome"]} jogou {x} partidas')
for c, i in enumerate(gol):
    print(f'   => Na partida {c+1}, fez {i} gols')
print(f'Totalizando {fut["total"]} gols')
