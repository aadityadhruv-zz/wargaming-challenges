import requests

url = 'http://www.enigmagroup.org/missions/programming/1/index.php'
cookies = {'enigmafiedV4': 'a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2236930%22%3Bi%3A1%3Bs%3A40%3A%22034233a09d11d67c4c56b214d7e23a3077140665%22%3Bi%3A2%3Bi%3A1586543529%3Bi%3A3%3Bi%3A2%3B%7D',
        'mission': 'yes' }

def solve_one():
    r = requests.get('http://ip.42.pl/raw')
    ip = r.content
    username = 'ThaWeatherman'
    data = {'ip': ip,
            'username': username
            }
    r = requests.post(url, cookies=cookies, data=data)
    print r.content

solve_one()
