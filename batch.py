from kamene.all import *

pcap_path = "c:\\Users\\taswi\\Desktop"
filename = str.join("\\", [pcap_path, "demo.pcap"])
packets = rdpcap(filename)


print(packets[672].time - packets[671].time)
#print(packets[671].__dict__)
print(packets[671].len/(packets[672].time - packets[671].time))
p = packets[671]
print(packets[671].tcp.