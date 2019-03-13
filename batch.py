from kamene.all import *

pcap_path = "/home/taswy/Code/Python/batch-wireshark"
filename = str.join("/", [pcap_path, "demo.pcap"])
packets = rdpcap(filename)


print(packets[672].time - packets[671].time)
#print(packets[671].__dict__)
print(packets[671].len/(packets[672].time - packets[671].time))
p = packets[671]
print(p)
