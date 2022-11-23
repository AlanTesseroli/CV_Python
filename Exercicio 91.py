from random import randint
from operator import itemgetter
print('Os jogos foram:')
ale = {'Jogador 1': randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1,6),
        'Jogador 4': randint(1,6)}
for c, i in ale.items():
        print(f'{c} jogou {i}')
ranking = sorted(ale.items(), key=itemgetter(1), reverse=True)
print('='*30)
print('O RANK FOI')
print('='*30)
for c, i in ranking:
        print(f'{c} = {i}')