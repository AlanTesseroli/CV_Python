# utilizamos a função de OPEN para abrir um arquivo, cujo argumento será o nome e onde se encontra o arquivo (como estou usando o mesmo diretório ele não encontra problemas)

# with serve para fechar o arquivo depois que não for mais necessário acessa-lo

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)