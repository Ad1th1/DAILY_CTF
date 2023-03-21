# #WolvCTF -> Charlotte's Web
# url = https://charlotte-tlejfksioa-ul.a.run.app/
# first go to url/src and then read the comment and do as directed

import requests

url = 'https://charlotte-tlejfksioa-ul.a.run.app/super-secret-route-nobody-will-guess'

x = requests.put(url)

print(x.text)
