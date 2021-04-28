We load up the site to see that it uses curl to check the status of the webpage

So we may be able to do RCE

So we try that and realise that the js blocks us so we hit the backend directly with `curl -X POST -F "ip=&&id" http://127.0.0.1:1337/api/curl`

We get no response, so looking at the code we can see it uses escapeshellcmd to escape the input we sent so thats not our vector.

Next we check LFI

Looking at the source shows us the flag is in `/flag` so if we request `file:///flag` then we should get the flag `curl -X POST -F "ip=file:///flag" http://127.0.0.1:1337/api/curl`

Putting that into the interface and we get the flag

CHTB{f1le_r3trieval_4s_a_s3rv1ce}
