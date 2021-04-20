from pwn import *
import re

# Connect
conn = remote('138.68.182.108', 32008)
print(conn.recvline().decode("utf-8"))
conn.recvuntil('>', drop=True)

# Enter the first option for our numbers
conn.send('1\n')
conn.recvline()
conn.recvline()

# Parse the given symbol to numbers
charMap = re.findall("(.) -> ([0-9]+)", conn.recvline().decode("utf-8"))
charNums = {}

for charSet in charMap:
    charNums[charSet[0]] = charSet[1]

print(charNums)

# Enter option 2
conn.recvuntil('>', drop=True)
conn.send('2\n')

# Parse the symbol equation
def fix(equ):
    out = ""
    for char in equ:
        if char in charNums:
            out += charNums[char]
        else:
            out += char
    return eval(out)

print(conn.recvline().decode("utf-8").strip())
print(conn.recvline().decode("utf-8").strip())
print(conn.recvline().decode("utf-8").strip())

# Loop over every question and answer them
while (True):
    print(conn.recvline().decode("utf-8").strip())
    print(conn.recvline().decode("utf-8").strip())
    equ = conn.recvline().decode("utf-8").replace(" = ?", "").strip()
    print("Q:" + equ)
    equ = fix(equ)
    print("A:" + str(equ))
    print(conn.recvuntil(':').decode("utf-8").strip())
    conn.send(str(equ) + '\n')
    print(conn.recvline().decode("utf-8").strip())
    print(conn.recvline().decode("utf-8").strip())
    print(conn.recvline().decode("utf-8").strip())

conn.close()