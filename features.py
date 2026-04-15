from scapy.all import IP, TCP, UDP
from datetime import datetime

def extract_packet_features(packet):
    if IP not in packet:
        return None

    feature = {
        "timestamp": datetime.now(),
        "src_ip": packet[IP].src,
        "dst_ip": packet[IP].dst,
        "packet_size": len(packet),
        "protocol": "OTHER",
        "src_port": None,
        "dst_port": None,
    }

    if TCP in packet:
        feature["protocol"] = "TCP"
        feature["src_port"] = packet[TCP].sport
        feature["dst_port"] = packet[TCP].dport
    elif UDP in packet:
        feature["protocol"] = "UDP"
        feature["src_port"] = packet[UDP].sport
        feature["dst_port"] = packet[UDP].dport

    return feature