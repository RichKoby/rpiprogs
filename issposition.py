import requests

url = "http://api.open-notify.org/iss-now.json"

r = requests.get(url)
j = r.json()
print(j)
print 'Position:',j['iss_position']['latitude'],',',j['iss_position']['longitude']

