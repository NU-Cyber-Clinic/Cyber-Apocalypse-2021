import binascii

keys_file = open('/Volumes/LaCie/keys.txt', 'rt')
flag = '0100000110001010010100010111010111000011100011001010111110001100000111001010111110101001001011001101111000000110010100111001110101010001001010000111000101100000010111010000011010110010110100000001101110111100000101101001011011110100111111110100100001111110100111010100011010111010000010110101101010101111011001011001100000000111'

ctr=0

for key in keys_file:
    key = key.rstrip().lstrip()
    # print(key)
    key_bin = bin(int(key, 16))[2:]
    if len(key_bin) % 8 != 0:
        key_bin = '0'*(8 - (len(key_bin) % 8)) + key_bin
    # print(key_bin)
    result = ''
    for i in range(40):
        result += '1' if key_bin[i] != flag[i] else '0'
    
    ascii_result = ''
    for i in range(0, 40, 8):
        ascii_result += chr(int(result[i:i+8], 2))

    # print(ascii_result)
    if 'CHTB' in ascii_result:
        print(f'Found CHTB with key\n {key} \n Preliminary result string: {ascii_result}')

    ctr += 1

    if ctr % 100000 == 0:
        print(f'\r{ctr} keys tried', end='')