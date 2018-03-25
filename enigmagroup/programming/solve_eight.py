import requests
from PIL import Image
# from pytesser import *

url = 'http://www.enigmagroup.org/missions/programming/8/image.php'
cookies = {'enigmafiedV4': 'a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2236930%22%3Bi%3A1%3Bs%3A40%3A%22034233a09d11d67c4c56b214d7e23a3077140665%22%3Bi%3A2%3Bi%3A1586543529%3Bi%3A3%3Bi%3A2%3B%7D'}

def solve_eight():
    s = requests.Session()
    r = s.get(url, cookies=cookies)
    with open('temp.png', 'w') as f:
        f.write(r.content)
    im = Image.open('temp.png')
    im_buf = im.load()
    # im = Image.open('temp.png')
    # rgb_im = im.convert('RGB')
    # width, height = im.size
    # for i in range(0,height):
    #     for j in range(0,width):
    #         r,g,b = rgb_im.getpixel((j,i))
    #         print r,g,b
    # im = Image.open('temp.png')
    # im2 = Image.new("P", im.size, 255)
    # im3 = im2.load()

    # for i in range(0,im.size[0]):
    #     for j in range(0,im.size[1]):
    #         pixel = im.getpixel((i,j))
    #         if pixel == 1 or pixel > 58:
    #             im3[i,j] = 1

    # im2.save('result.png', 'PNG')
    # answer = image_to_string(im2)
    # print answer

solve_eight()
