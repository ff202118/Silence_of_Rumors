import requests

url = 'https://www.httpcn.com'
r = requests.get(url)
r.encoding = 'utf-8'
# print(r.status_code, r.encoding, r.cookies, r.headers, r.text)

print(r.text)
