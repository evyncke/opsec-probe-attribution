#!/usr/bin/env python3

from scapy.all import *

interface = "en7"
source = "2001:db8:dead::1"
destination = "2001:db8:beef::1"

ip6DH = IPv6ExtHdrDestOpt(options=PadN(optdata=b"https://example.net/.well-known/probing.txt" + b"\0")) / TCP(sport=RandShort(), dport=33434, flags="S")
wrpcap('examples.pcap', IPv6(src=source, dst=destination) / ip6DH)
ip6TCP = TCP(sport=RandShort(), dport=33434, flags="S") / (b"mailto:lab@example.net" + b"\0")
wrpcap('examples.pcap', IPv6(src=source, dst=destination) / ip6TCP, append=True)
ip6ICMP = ICMPv6EchoReply(data=b"tel:+1-201-555-0123" + b"\0")
wrpcap('examples.pcap', IPv6(src=source, dst=destination) / ip6ICMP, append=True)

# Let's also make one legacy IPv4 example
source4 = "192.0.2.1"
destination4 = "198.51.100.1"

ip4ICMP = ICMP(type=8, code=0) / (b"mailto:lab@example.net" + b"\0")
wrpcap('examples4.pcap', IP(src=source4, dst=destination4) / ip4ICMP)

# Those examples can then be dumped nicely with:
#  tcpdump -r examples.pcap -X -t > examples.txt
#  tcpdump -r examples4.pcap -X -t > examples4.txt