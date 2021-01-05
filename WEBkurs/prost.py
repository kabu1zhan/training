import requests
import json
url1 = 'https://datasend.webpython.graders.eldf.ru/submissions/super/duper/secret/'
url = 'https://datasend.webpython.graders.eldf.ru/submissions/1/'
headers = {'Authorization': 'Basic YWxsYWRpbjpvcGVuc2VzYW1l'}

r = requests.post(url, headers=headers)
print(json.loads(r.content.decode('utf-8')))
header1 = {'Authorization': 'Basic Z2FsY2hvbm9rOmt0b3RhbWE='}
r1 = requests.put(url1, headers=header1)
print(r1.content)
with open('answer.txt', 'w') as f:
    f.write(r1.json()['answer'])
