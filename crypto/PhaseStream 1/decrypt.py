def sxor(s1,s2):    
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

cipher = '2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904'

final_string = ''

for i in range(256):
    final_string = chr(i)*5*11
    print(sxor(cipher, final_string))

print(len(cipher))
print(len(final_string))