1. Instead of hardcoded seeds, it now uses system time. Unix Epoch to be precise
2. From the metadata of the file we can see it was last modified on the 16th April 2021 at 12:32:16
3. Go to [epochconverter.com](https://www.epochconverter.com) and find the epoch times for 16th April 2021 12:32:16 and 16th April 2020 12:32:16
4. Wrote a script that generates the XOR key for every second in the last year (31-32 million keys). 
5. The keys file was 2.3GB large so i won't upload it to git. To generate it for yourself cd into solve and run 
```bash
cargo run
```
6. Then put those keys to good use by trying each and every one of them. For performance purposes it'll test the first 5 characters only and looks for CHTB.
7. Finds it between keys 31miln-32miln