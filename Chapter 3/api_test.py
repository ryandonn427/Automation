import requests
result = requests.get('https://jsonplaceholder.typicode.com/posts')
print(result.json()[-1])

new_post = {'userId':10,'title':'a title','body':'something something'}
result = requests.post('https://jsonplaceholder.typicode.com/posts',json=new_post)
print(result.json())
print(result.headers['Location'])

update = {'body':'new body'}
result = requests.patch('https://jsonplaceholder.typicode.com/posts/2',json=update)
print(result.json())