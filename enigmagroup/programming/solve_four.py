import requests
from PIL import Image

referer = 'http://www.enigmagroup.org/missions/programming/4/index.php'
url = 'http://www.enigmagroup.org/missions/programming/4/image.php'
cookies = {'enigmafiedV4': 'a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2236930%22%3Bi%3A1%3Bs%3A40%3A%22034233a09d11d67c4c56b214d7e23a3077140665%22%3Bi%3A2%3Bi%3A1586543529%3Bi%3A3%3Bi%3A2%3B%7D'}

def solve_four():
    s = requests.Session()
    s.headers.update({'referer': referer})
    r = s.get(url, cookies=cookies)
    # print r.content
    with open('temp.png', 'w') as f:
        f.write(r.content)
    im = Image.open('temp.png')
    rgb_im = im.convert('RGB')
    width, height = im.size
    binary = ''
    for i in range(0,height):
        for j in range(0,width):
            r,g,b = rgb_im.getpixel((j,i))
            # print r,g,b
            if r:
                binary += '0'
            else:
                binary += '1'
    totes = height*width
    x = 0
    answer = ''
    while x < totes:
        substring = binary[x:x+8]
        num = int(substring, 2)
        if num < 128:
            answer += chr(num)
        x += 8
    print answer
    idx = answer.find(':')
    answer = answer[idx+1:]
    print answer
    r = s.post(url, cookies=cookies, data={'answer': answer})
    print r.content

solve_four()
