import requests
from bs4 import BeautifulSoup
import re

response = requests.get('https://httpbin.org/forms/post')
page = BeautifulSoup(response.text)
form = page.find('form')
print({field.get('name') for field in form.find_all(re.compile('input|textarea'))})
data = {'custname':"Sean O'Connell",'custtel':'123-456-789',
'custemail':'sean@oconnel.ie','size':'small','topping':['bacon','onion'],'delivery':'20:30','comments':''}
response = requests.post('https://httpbin.org/post',data)
print(response.json())