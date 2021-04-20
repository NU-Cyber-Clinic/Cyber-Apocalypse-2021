from scapy.all import *

capture = rdpcap('older_trick.pcap')

ascii = [p[ICMP].load[16:][:16] for p in capture if p.haslayer(ICMP) and p[ICMP].type == 8]

with open('out.zip', 'wb') as f:
    for x in ascii:
        f.write(x)