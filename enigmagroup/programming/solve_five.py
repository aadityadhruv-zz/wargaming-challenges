import requests, re, subprocess, os

cookies = {'enigmafiedV4': 'a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2236930%22%3Bi%3A1%3Bs%3A40%3A%22034233a09d11d67c4c56b214d7e23a3077140665%22%3Bi%3A2%3Bi%3A1586543529%3Bi%3A3%3Bi%3A2%3B%7D'}
headers = {'referer': 'http://www.enigmagroup.org/missions/programming/5/'}
url = 'http://www.enigmagroup.org/missions/programming/5/index.php'

def solve_five(): 
    s = requests.Session()
    r = s.get(url, cookies=cookies)
    m = re.search('<br />[[\]<>.,+-]+<br />', r.content) 
    gotit = m.group(0) 
    gotit = gotit[6:] 
    thecode = gotit[:-6] 
    with open('brainfuck.txt','w') as f: 
        f.write(thecode) 
    full_path = os.path.abspath('brainfuck.py') 
    p = subprocess.Popen([full_path, 'brainfuck.txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    out, err= p.communicate()
    out = out.strip() 
    headers = { 'referer': referer } 
    r = s.get(url, cookies=cookies, headers=headers, params={'ans': out})
    print r.content

solve_five()
