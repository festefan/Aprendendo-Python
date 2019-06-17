import requests
from bs4 import BeautifulSoup

pagina = requests.get('http://www.uninove.br')

sopa = BeautifulSoup(pagina.text, 'html.parser')


#encontra todos os links

uninove = sopa.find_all('a')

for i in uninove:
    print(i.get('href'))

input('')
print(sopa.find_all('p')[2].get_text())
 
print(sopa.find_all('p')[4].get_text())
 
