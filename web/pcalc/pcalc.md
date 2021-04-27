As we cant use alpha chars my first thaught was phpfuck

But due to the 100 char limit thats not possible

So i did some searching, and came over https://www.php.net/manual/en/language.operators.execution.php which states `\``can be used for running shell commands

Combineing this with wildcards we can run commands like cat

https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/x11655.htm

```php
`/???/??? /*`
```
equates to
```bash
/bin/cat /*
```

CHTB{I_d0nt_n33d_puny_hum4n_l3tt3rs_t0_pwn!}
