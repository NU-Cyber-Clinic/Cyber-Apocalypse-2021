from bitstring import BitArray

# CTR explainer: https://pycryptodome.readthedocs.io/en/latest/src/util/util.html#crypto-util-counter-module

test = b"No right of private conversation was enumerated in the Constitution. I don't suppose it occurred to anyone at the time that it could be prevented."
test_bin = BitArray(test).bin
encrypted = "464851522838603926f4422a4ca6d81b02f351b454e6f968a324fcc77da30cf979eec57c8675de3bb92f6c21730607066226780a8d4539fcf67f9f5589d150a6c7867140b5a63de2971dc209f480c270882194f288167ed910b64cf627ea6392456fa1b648afd0b239b59652baedc595d4f87634cf7ec4262f8c9581d7f56dc6f836cfe696518ce434ef4616431d4d1b361c"
encrypted_bin = BitArray(hex=encrypted).bin

print(test_bin)
print(encrypted_bin)
print()
print()
print()

block = []
test_block = []

for i in range(146*8):
    block.append( '1' if test_bin[i] != encrypted_bin[i] else '0')
    

block_hex = BitArray(bin=''.join(block)).hex

print(block_hex)


