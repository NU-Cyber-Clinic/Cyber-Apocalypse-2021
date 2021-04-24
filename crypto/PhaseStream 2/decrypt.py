#Python 2.7

def sxor(s1,s2):    
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

cipher_file = open('output.txt')

counter = 0
for cipher in cipher_file:
    for i in range(256):
        key = chr(i)*55
        decoded_cipher = cipher.lstrip().rstrip().decode("hex")
        plain = sxor(decoded_cipher, key)
        if 'CHTB{' in plain:
            print(plain)
    counter += 1
    if counter % 1000 == 0:
        print "Passed line " + str(counter)