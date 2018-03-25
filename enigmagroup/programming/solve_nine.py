import requests
from bs4 import BeautifulSoup
import numpy as np

url = 'http://www.enigmagroup.org/missions/programming/9/index.php'
cookies = {'enigmafiedV4': 'a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2236930%22%3Bi%3A1%3Bs%3A40%3A%22034233a09d11d67c4c56b214d7e23a3077140665%22%3Bi%3A2%3Bi%3A1586543529%3Bi%3A3%3Bi%3A2%3B%7D'}

def what_shape(src):
    if 'triangle' in src:
        return 't'
    elif 'circle' in src:
        return 'c'
    elif 'heart' in src:
        return 'h'
    elif 'star' in src:
        return 's'
    elif 'square' in src:
        return 'q'

def get_equations(tds, eq_num):
    eq_dict = {'t': 0, 'c': 0, 'h': 0, 's': 0, 'q': 0, 'total': 0}
    start = 0 if eq_num == 1 else (eq_num-1) * 6
    end = start + 6
    for i in range(start, end):
        img = tds[i].find('img')
        if img == None:
            strong = tds[i].find('strong')
            if strong != None:
                total = int(strong.text)
                eq_dict['total'] = total
        else:
            shape = what_shape(img.attrs['src'])
            eq_dict[shape] += 1
    return eq_dict

def create_equation(eq_dict):
    eq = []
    eq.append(eq_dict['t'])
    eq.append(eq_dict['c'])
    eq.append(eq_dict['h'])
    eq.append(eq_dict['s'])
    eq.append(eq_dict['q'])
    return (eq, eq_dict['total'])

def solve_nine():
    s = requests.Session()
    r = s.get(url, cookies=cookies)
    soup = BeautifulSoup(r.content)
    table = soup.find('table')
    tds = table.find_all('td')
    eq1_dict = get_equations(tds, 1)
    eq2_dict = get_equations(tds, 2)
    eq3_dict = get_equations(tds, 3)
    eq4_dict = get_equations(tds, 4)
    eq5_dict = get_equations(tds, 5)
    eq1, eq1_total = create_equation(eq1_dict)
    eq2, eq2_total = create_equation(eq2_dict)
    eq3, eq3_total = create_equation(eq3_dict)
    eq4, eq4_total = create_equation(eq4_dict)
    eq5, eq5_total = create_equation(eq5_dict)
    a = np.array([ eq1, eq2, eq3, eq4, eq5 ])
    b = np.array([ eq1_total, eq2_total, eq3_total, eq4_total, eq5_total ])
    # print a
    # print b
    x = np.linalg.solve(a,b)
    l = x.tolist()
    l = [ int(y) for y in l ]
    # print l
    data = { 'circle': l[1], 'heart': l[2], 'square': l[4], 'triangle': l[0], 'star': l[3], 'submit': 'Submit' }
    r = s.post(url, cookies=cookies, data=data)
    print r.content

solve_nine()
