def leitura_arquivo(arquivo):
    try:
        with open(arquivo, 'r') as file_object:
            leitura = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(leitura)

gatos = leitura_arquivo('cats.txt')
cachorros = leitura_arquivo('dogs.txt')