with open('10.3 to 10.5.txt', 'w') as file_object:
    file_object.write('Atividade 10.3   -->  ' + str(input('Qual seu nome: ')) + '\n')
    file_object.close()

with open('10.3 to 10.5.txt', 'a') as file_object:
    file_object.write('ATIVIDADE 10.4' + '\n')
    while True:
        print('Para sair digite 1')
        nome = str(input('Qual seu nome: '))
        if nome == '1':
            break
        else:
            print(f'Olá, {nome}, que bom que você veio!')
            file_object.write(nome + '\n')
file_object.close()

with open('10.3 to 10.5.txt', 'a') as file_object:
    file_object.write('ATIVIDADE 10.5' + '\n')
    while True:
        print('Para sair digite 1')
        resposta = str(input('Porque você gosta de programação: '))
        if resposta == '1':
            break
        else:
            print(f'Excelente motivo! Muito obrigado!')
            file_object.write('Motivo --> ' + resposta + '\n')
file_object.close()