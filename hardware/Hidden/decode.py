filename = 'encoded_flag.txt'

file = open(filename, 'rt')

flag = file.readline().lstrip().rstrip()
flag = bytes.fromhex(flag)

next_in_seq = int('2E9D3', 16)

def keygen():
    global next_in_seq
    next_in_seq = 50550653 * next_in_seq + 5210
    return next_in_seq % 255

left_half = 0
right_half = 0

#Front to back, check if the flag is above 0x10
for x in range(0,200,1):
    next_in_seq = int('2E9D3', 16)
    result = ''
    for i in range(x,200, 1):
        # i = 199 - i
        if flag[i] > 16:
            continue

        if i % 2 == 0:
            left_half = ((flag[i]-1) << 4 )
            # print(bin(left_half))
        else:
            right_half = (flag[i]-1)
            # print(bin(right_half))

            result += chr( keygen() ^ ((left_half+right_half) & 255)  )
    if 'CHTB' in result:
        print(result)

#Front to back, don't check if the flag is above 0x10
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

#Back to front, check if the flag is above 0x10
for x in range(0,200,1):
    next_in_seq = int('2E9D3', 16)
    result = ''
    for i in range(x,200, 1):
        i = 199 - i
        if flag[i] > 16:
            continue

        if i % 2 == 0:
            left_half = ((flag[i]-1) << 4 )
            # print(bin(left_half))
        else:
            right_half = (flag[i]-1)
            # print(bin(right_half))

            result += chr( keygen() ^ ((left_half+right_half) & 255)  )
    if 'CHTB' in result:
        print(result)

#Back to front, don't check if the flag is above 0x10
for x in range(0,200,1):
    next_in_seq = int('2E9D3', 16)
    result = ''
    for i in range(x,200, 1):
        i = 199 - i
        # if flag[i] > 16:
        #     continue

        if i % 2 == 0:
            left_half = ((flag[i]-1) << 4 )
            # print(bin(left_half))
        else:
            right_half = (flag[i]-1)

            result += chr( keygen() ^ ((left_half+right_half) & 255)  )
    if 'CHTB' in result:
        print(result)