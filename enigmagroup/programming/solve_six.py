import requests, string
from bs4 import BeautifulSoup

url = 'http://www.enigmagroup.org/missions/programming/6/'
submit_url = url + 'submit.php'
cookies = {'enigmafiedV4': 'a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2236930%22%3Bi%3A1%3Bs%3A40%3A%22034233a09d11d67c4c56b214d7e23a3077140665%22%3Bi%3A2%3Bi%3A1586543529%3Bi%3A3%3Bi%3A2%3B%7D'}

def to_normal_string(the_str):
    return ''.join(chr(ord(c)) for c in the_str)

def dictionary(wordlist):
    dicti = []
    infile = open(wordlist, "r")
    for line in infile:
        word = line.strip()
        dicti.append(word)
    infile.close()
    return dicti

def count_chars(the_str):
    ret_dict = {}
    for c in the_str:
        if not ret_dict.has_key(c):
            ret_dict[c] = 1
        else:
            ret_dict[c] += 1
    return ret_dict

def solve_six():
    s = requests.Session()
    r = s.get(url, cookies=cookies)
    soup = BeautifulSoup(r.content)
    para_text = soup.find('p').text
    anas = [to_normal_string(x) for x in para_text.split('\n')]
    diction = dictionary('keywords.txt')
    answers = []
    for ana in anas:
        ana_len = len(ana)
        ana_dict = count_chars(ana)
        for entry in diction:
            if len(entry) != ana_len:
                continue
            entry_dict = count_chars(entry)
            if ana_dict == entry_dict:
                answers.append(entry)
                break
    answer_str = ''
    for answer in answers:
        answer_str += answer + ','
    answer_str = answer_str[:-1]
    data = {'anagram': answer_str,
            'submit': 'true'
            }
    r = s.post(submit_url, cookies=cookies, data=data)
    print r.content

solve_six()
