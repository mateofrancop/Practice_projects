import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/')


sopa = bs4.BeautifulSoup(resultado.text, 'lxml')


print(sopa)
