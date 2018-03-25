import requests
from bs4 import BeautifulSoup

cookies = {'enigmafiedV4': 'a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2236930%22%3Bi%3A1%3Bs%3A40%3A%22034233a09d11d67c4c56b214d7e23a3077140665%22%3Bi%3A2%3Bi%3A1586543529%3Bi%3A3%3Bi%3A2%3B%7D'}
url = 'http://www.enigmagroup.org/missions/programming/2/index.php'

def solve_two():
    s = requests.Session()
    r = s.get(url, cookies=cookies)
    soup = BeautifulSoup(r.content)
    inputs = soup.find_all('input')
    rand_num = int(inputs[1].attrs['value'])
    ans = rand_num * 4
    data = { 'answer': str(ans),
            'E[number]': str(rand_num),
            'E[time]': inputs[2].attrs['value'],
            'hash': inputs[3].attrs['value'],
            'submit': 'Submit Answer' }
    r = s.post(url, cookies=cookies, data=data)
    print r.content

solve_two()
