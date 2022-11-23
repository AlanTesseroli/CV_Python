def area(l, c):
    print(f'Um terreno de {l}m x {c}m tem {l*c}m2 de área')


print('CONTROLE DE TERRENOS')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l,c)