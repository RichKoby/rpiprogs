import requests

url = "http://api.open-notify.org/astros.json"

r = requests.get(url)
j = r.json()
n = j['number']
#print(j)
print 'There are',n,'people currently in space.  They are:'
for i in range(n):
    print 'Name:',j['people'][i]['name'],'Craft:',j['people'][i]['craft']

