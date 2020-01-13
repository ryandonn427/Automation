import requests

print(requests.get('https://httpbin.org/basic-auth/user/passwd',auth=('user','psswd')))

print(requests.get('https://httpbin.org/basic-auth/user/passwd',auth = ('user','wrong')))

print(requests.get('https://user:psswd@httpbin.org/basic-auth/user/passwd'))

print(requests.get('https://user:wrong@httpbin.org/basic-auth/user/passwd'))

