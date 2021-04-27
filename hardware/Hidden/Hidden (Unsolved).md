# (STILL) HIDDEN

## The files
    * firmware - ARM32 ELF binary (that won't run ARM CPUs lol)
    * hidden.sal - Logic 2 file with two channels, looks like async serial

## The tools

Spend 3 hours looking at ARM documentation, cheat sheets and machine code and after trying to open it in 6 different disassembly software, simply ask your mate to open the binary in IDA Pro and grab the pseudocode for you. Some python too but it's everywhere at this point.

## The binary

1. Hardcoded flag, 50 characters long
2. Iterate through the flag string and XOR each character with a freshly generated key, stored in the *next_in_seq* variable. 

```cpp
unsigned int next_in_seq = 0x2E9D3;
unsigned int key_generator()
{
  next_in_seq = 50550653 * next_in_seq + 5210;
  return next_in_seq % 0xFFu; //0xFFu means 0xFF unsigned => 255
}
```

Store the new string somewhere in memory.  
    * It was stored at some offset address in the *buf* variable but not quite. It was weird and a lot of time was wasted there. Make what you will of "(*((_BYTE *)&buf[100] + i)"

3. Open the write stream to for termio with a file given via argv
```cpp
fd = open(argv[1], 2306);
```
4. Set the flags for termio
5. This is the important part: Iterate again through the buffer with the XORed flag, but split each characters in two chunks.
```cpp
counter = 0;
for ( i = 0; i <= 49; ++i )
{
    buf[counter] = ((*((_BYTE *)&buf[100] + i) >> 4) & 0xF) + 1; // 1
    buf[counter + 1] = (*((_BYTE *)&buf[100] + i) & 0xF) + 1; // 2
    counter += 2;
}
```

First of all, take note that the the values assigned to the buffer are by counter, not by the for iterator index i.

At comment 1, the character at each index in the weird place in the buffer is bitshifted to the right (>>) by 4 bits and ANDed with 0xF to remove the first 4 bits of the char for good. Essentially moving the first half of the byte to the right. Then add 1 for extra spice. 

At comment 2, the same character is just ANDed with 0xF to preserve the last 4 bits and add 1 for extra spice. 

What this essentially does is it splits the character byte into two characters that later have to be put back together.

This means a few things:
    * All characters have a maximum value of 0x10
    * The resulting string is len(flag)*2 = 50 * 2 = 100 bytes. 101 If you count EOF.
    * The hex digit length should be 200 then.
    * The 4 most significant bits are on even indexes, while the 4 least significant bits are on odd indexes

6.  Write the new buffer to the device, then close the stream and call it the day.

## The signal file

1. The HTB gods have attached a signal file that can be opened in Logic 2 and analysed.
2. It has two channels, but only one seems to have been active. 
3. The active channel seems to by async serial.
4. Some digging around gives us the default baud rate for termio to be 38400 bits/s. 
5. This is where we had some issues:
* With all the switches set to default => a hex encoded string that has a lot of values above 0x10
* With inverted signal => Hex values that are much larger than 0x10, but the string ends in \0 which might be a sign of an outputted string

## The (possible) solution

We want to create a decoder for that reverses the firmware's actions and reads the encoded data extracted from the signal file.

1. Read the flag hexdecimal, strip it of any possible whitespace and decode it from hex into a byte array

```py
filename = 'encoded_flag.txt'

file = open(filename, 'rt')

flag = file.readline().lstrip().rstrip()
flag = bytes.fromhex(flag)
```

2. Copy the key generation module from the decompiled version. Since XOR's inverse function is XOR, we must use the same keygen to properly recreate the encoding process.

```py
next_in_seq = int('2E9D3', 16)

def keygen():
    global next_in_seq
    next_in_seq = 50550653 * next_in_seq + 5210
    return next_in_seq % 255
```

3. Now we want to iterate through the encoded data and to join the left and right half of each character. From the code explainer, the left halves are on even indexes, while their corresponding right halves are one index higher on odd indexes. We also know that we have to subtract that spicy 1 and that it has been XORed in the beginning, so we're going to XOR at the end. We're going to iterate through 200 bytes instead of 100 because that's how long the extracted data is. 

```py
for i in range(0,200, 1):
        if i % 2 == 0:
            left_half = ((flag[i]-1) << 4 )
            # print(bin(left_half))
        else:
            right_half = (flag[i]-1) % 255
            # print(bin(right_half))

            result += chr( keygen() ^ ((left_half+right_half) & 255)  )
```

4. We can try and filter out the characters that are higher than 0x10:

```py
for i in range(0,200, 1):
        if flag[i] > 16:
            continue

        if i % 2 == 0:
            left_half = ((flag[i]-1) << 4 )
            # print(bin(left_half))
        else:
            right_half = (flag[i]-1) % 255
            # print(bin(right_half))
            result += chr( keygen() ^ ((left_half+right_half) & 255)  )
```

5. We can also try to process the encoded cipher from the last byte to the first

```py
for i in range(0,200, 1):
        i = 199 - i

        if i % 2 == 0:
            left_half = ((flag[i]-1) << 4 )
            # print(bin(left_half))
        else:
            right_half = (flag[i]-1) % 255
            # print(bin(right_half))

            result += chr( keygen() ^ ((left_half+right_half) & 255)  )
```

5. Since extracted data is longer than expected, the flag can be anywhere in the string. This also means that there is a possibility, although not certain, that the flag may have been encrypted separately or has some padding around it. As an extra step to ensure we haven't missed anything, we're trying to decipher starting from varying points in the encoded cipher.

```py
for x in range(0,200,1):
    next_in_seq = int('2E9D3', 16)
    result = ''
    for i in range(x,200, 1):
        # i = 199 - i
        # if flag[i] > 16:
        #     continue

        if i % 2 == 0:
            left_half = ((flag[i]-1) << 4 )
            # print(bin(left_half))
        else:
            right_half = (flag[i]-1) % 255
            # print(bin(right_half))

            result += chr( keygen() ^ ((left_half+right_half) & 255)  )
    if 'CHTB' in result:
        print(result)
```

6. The decoded.py file has all the permutations of these settings 