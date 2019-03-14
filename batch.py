#coding=utf-8
from kamene.all import *

class Packet():
    def __init__(self, pcap_packet):
        self.src_ip = pcap_packet.src
        self.dest_ip = pcap_packet.dst
        self.src_port = pcap_packet.sport
        self.dest_port = pcap_packet.dport
        self.proto = pcap_packet.proto
        self.send_time = pcap_packet.sent_time
        self.receive_time = pcap_packet.time
        self.len = pcap_packet.len
        return super().__init__()
    
    def __str__(self):
        return "src_ip: {}, dest_ip: {}, src_port: {}, dest_port: {}, proto: {}, send_time: {}, receive_time: {}"\
            .format(self.src_ip, self.dest_ip, self.src_port, self.dest_port, self.proto, self.send_time, self.receive_time )

if __name__ == "__main__":
    pcap_path = "/home/taswy/Code/Python/batch-wireshark"
    filename = str.join("/", [pcap_path, "demo.pcap"])
    packets = rdpcap(filename)
    len_acc = 0
    for p in packets:
        packet = Packet(p)
        len_acc += packet.len
        print(packet)
    print("length of this communication:", len_acc)