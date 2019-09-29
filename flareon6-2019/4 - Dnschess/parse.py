from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, DNSRR
from pprint import pprint

dns_packets = rdpcap("./capture.pcap")

res = []
for pkt in dns_packets:
    if pkt.haslayer(DNS):
        udp = pkt['UDP']
        dns = pkt['DNS']

        if int(udp.sport) == 53:
            for i in range(dns.ancount):
                dnsrr = dns.an[i]
                # print(dnsrr.rrname, dnsrr.rdata)
                res.append((dnsrr.rrname, dnsrr.rdata))


# print(res)
moves = []
for i in res:
    ip0, ip1, ip2, ip3 = [int(j) for j in i[1].split('.')]
    if ip0 == 127 and (ip3 & 1) == 0:
        moves.append((ip2 & 0xF, i[0]))

moves.sort()
for i in moves:
    print(i)

'''
(0, b'pawn-d2-d4.game-of-thrones.flare-on.com.')
(1, b'pawn-c2-c4.game-of-thrones.flare-on.com.')
(2, b'knight-b1-c3.game-of-thrones.flare-on.com.')
(3, b'pawn-e2-e4.game-of-thrones.flare-on.com.')
(4, b'knight-g1-f3.game-of-thrones.flare-on.com.')
(5, b'bishop-c1-f4.game-of-thrones.flare-on.com.')
(6, b'bishop-f1-e2.game-of-thrones.flare-on.com.')
(7, b'bishop-e2-f3.game-of-thrones.flare-on.com.')
(8, b'bishop-f4-g3.game-of-thrones.flare-on.com.')
(9, b'pawn-e4-e5.game-of-thrones.flare-on.com.')
(10, b'bishop-f3-c6.game-of-thrones.flare-on.com.')
(11, b'bishop-c6-a8.game-of-thrones.flare-on.com.')
(12, b'pawn-e5-e6.game-of-thrones.flare-on.com.')
(13, b'queen-d1-h5.game-of-thrones.flare-on.com.')
(14, b'queen-h5-f7.game-of-thrones.flare-on.com.')
'''