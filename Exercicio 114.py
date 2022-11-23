import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError :
    print('O site pudim não está acessível no momento')
else:
    print('Consegui acessar o site com sucesso')