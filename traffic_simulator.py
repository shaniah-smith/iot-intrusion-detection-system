from scapy.all import IP, TCP, UDP, send
import random
import time


def simulate_normal_traffic(target_ip, duration=10):
    print("Simulating normal traffic...")
    end_time = time.time() + duration

    while time.time() < end_time:
        packet = IP(dst=target_ip) / TCP(
            sport=random.randint(1024, 65535),
            dport=random.choice([80, 443, 53])
        )
        send(packet, verbose=False)
        time.sleep(0.5)


def simulate_dos_traffic(target_ip, duration=5):
    print("Simulating DoS-like traffic...")
    end_time = time.time() + duration

    while time.time() < end_time:
        packet = IP(dst=target_ip) / UDP(
            sport=random.randint(1024, 65535),
            dport=80
        )
        send(packet, verbose=False)


def simulate_port_scan(target_ip):
    print("Simulating port scan...")
    for port in range(20, 120):
        packet = IP(dst=target_ip) / TCP(
            sport=random.randint(1024, 65535),
            dport=port
        )
        send(packet, verbose=False)
        time.sleep(0.05)