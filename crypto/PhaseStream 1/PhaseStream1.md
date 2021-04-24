1. The cipher has been XORed with a repeating 5 byte sequence
2. Each flag starts with CHTB{ which is precisely 5 bytes long
3. Use CyberChef to decode from hex and XOR that to find the key (it's literally mykey)
4. XOR the cipher with mykey
5. CHTB{u51ng_kn0wn_pl41nt3xt}