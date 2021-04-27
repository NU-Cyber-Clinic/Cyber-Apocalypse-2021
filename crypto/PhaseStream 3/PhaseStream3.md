1. The aliens are using AES in CTR mode
2. There is a test string with output. Seems to be a quote from Witfield Diffie or whatever his name is
3. We can use this to do a known-plaintext attack, but it'd take ages
4. The code reuses the same key for both and runs AES in CTR with no IV
5. Even if it is 128-bit, CTR still uses XOR. So if the key is the same, it's practically using just the same XOR twice. 
6. CyberChef ftw. 
7. CHTB{r3u53d_k3Y_4TT4cK}
