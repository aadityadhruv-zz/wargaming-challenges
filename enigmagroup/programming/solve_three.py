import requests
from PIL import Image

cookies = {'enigmafiedV4': 'a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2236930%22%3Bi%3A1%3Bs%3A40%3A%22034233a09d11d67c4c56b214d7e23a3077140665%22%3Bi%3A2%3Bi%3A1586543529%3Bi%3A3%3Bi%3A2%3B%7D'}
url = 'http://www.enigmagroup.org/missions/programming/3/image.php'
referer = 'http://www.enigmagroup.org/missions/programming/3/image.php'

def solve_three():
    s = requests.Session()
    s.headers.update({'referer':referer})
    r = s.get(url, cookies=cookies)
    with open('temp.jpeg','w') as f:
        f.write(r.content)
    im = Image.open('temp.jpeg')
    rgb_im = im.convert('RGB')
    r,g,b = rgb_im.getpixel((1,1))
    color_param = '%d;%d;%d' % (r,g,b)
    r = s.post(url, cookies=cookies, data={'color': color_param, 'submit': '1'})
    print r.content

solve_three()
