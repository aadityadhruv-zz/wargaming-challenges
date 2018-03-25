import re, requests
from bs4 import BeautifulSoup

cookies = {'enigmafiedV4': 'a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2236930%22%3Bi%3A1%3Bs%3A40%3A%22034233a09d11d67c4c56b214d7e23a3077140665%22%3Bi%3A2%3Bi%3A1586543529%3Bi%3A3%3Bi%3A2%3B%7D'}
headers = {'referer': 'http://www.enigmagroup.org/missions/programming/7/'}
url = 'http://www.enigmagroup.org/missions/programming/7/'
submit_url = 'http://www.enigmagroup.org/missions/programming/7/submit.php'

def get_company_name(text):
    m = re.search('We need you to steal data from the [A-Za-z]+ department.', text)
    str = m.group(0)
    strip_str = 'We need you to steal data from the '
    the_name = str[len(strip_str):]
    the_len = len(' department.')
    the_len = -the_len
    return the_name[:the_len]

def to_normal_string(str):
    return ''.join(chr(ord(c)) for c in str)

def strip_leading_text(all_m, pattern):
    nums = []
    for m in all_m:
        m = to_normal_string(m)
        m = int(m[len(pattern):])
        nums.append(m)
    return nums

def get_all_budgets(text, pattern):
    all_m = re.findall(pattern, text)
    return all_m

s = requests.Session()
r = s.get(url, cookies=cookies)
soup = BeautifulSoup(r.content)
divs = soup.find_all('div')
text = divs[1].text
dept = to_normal_string(get_company_name(text))
pattern = '%s Monthly Budget: \$[0-9]+' % dept
all_m = get_all_budgets(text, pattern)
pattern = '%s Monthly Budget: $' % dept
nums = strip_leading_text(all_m, pattern)
total = 0
for num in nums:
    total += num

para_text = soup.find('p').text
idx = para_text.find('C')
begin = para_text[idx:idx+19]
cmpy = begin[10:]
# m = re.search('Company: .+D', para_text)
# found = m.group(0)
# print found
# idx = found.find('<')
# remove_idx = len(found)-idx
# remove_idx = -remove_idx
# found = found[:remove_idx]
data = {'company': cmpy, 'department': dept, 'total': str(total)}
r = s.post(submit_url, headers=headers, cookies=cookies, data=data)
print r.content
