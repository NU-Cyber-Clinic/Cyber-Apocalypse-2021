1. Same as PhaseStream3, AES in CTR with reused key, but now we don't have any plaintext.
2. We know the first 5 characters of the flag cipher
3. XOR-ing that will get us the string 'I alo'. Not very specific.
4. The previous test plaintext was a quote by Whitfield Diffie (is that his name?). Quoted by Bruce Schenier too
5. Heading over to google we find a quote by mother theresa (which seems to be fake after all but who gives a shit at this point it's 2am after a long day and i'm still writing documentation)
```I alone cannot change the world, but I can cast a stone across the waters to create many ripples.```
```
https://www.pinterest.com/pin/574983077405224762/
https://www.entrepreneur.com/article/254232
```
5. ^ This is test plaintext
6. XOR that with the test cipher, grab the result and use it as a key to decipher the flag cipher
7. CyberChef ftw.
8. CHTB{stream_ciphers_with_reused_keystreams_are_vulnerable_to_known_plaintext_attacks}