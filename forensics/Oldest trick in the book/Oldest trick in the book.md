Pcap file with the data being hidden in the ICMP packets

I read 16 bytes of each packets data and read 16 bytes from there

Constructing the data back together gives a zip file

Within that zip there is firefox user data which contains login info for a rabbitmq site

Decrypting that data with something like https://github.com/lclevy/firepwd gives the key as the password

CHTB{long_time_no_s33_icmp}
