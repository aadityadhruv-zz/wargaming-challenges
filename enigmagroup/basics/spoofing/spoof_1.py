import requests

# uses proxy through china (low anonymous proxy)
http_proxy = 'http://119.97.146.16:8080'
url = 'http://www.enigmagroup.org/missions/basics/spoof/1/'
cookies = {'enigmafiedV4': 'a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2236930%22%3Bi%3A1%3Bs%3A40%3A%22034233a09d11d67c4c56b214d7e23a3077140665%22%3Bi%3A2%3Bi%3A1586543529%3Bi%3A3%3Bi%3A2%3B%7D'}
r = requests.get(url, cookies=cookies, proxies={'http': http_proxy})
print r.content
