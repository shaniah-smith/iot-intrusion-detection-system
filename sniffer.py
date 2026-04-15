from scapy.all import sniff
from features import extract_packet_features
from detector import SimpleWindowDetector, RuleBasedIDS
from utils import save_result_to_csv

window_detector = SimpleWindowDetector(window_size=5)
ids = RuleBasedIDS()


def process_packet(packet):
    feature = extract_packet_features(packet)

    if feature:
        stats = window_detector.add_packet(feature)

        if stats:
            result = ids.detect(stats)

            print("=" * 60)
            print(result["label"])
            print(result["stats"])

            if result["reasons"]:
                for reason in result["reasons"]:
                    print("Reason:", reason)

            print("=" * 60)

            row = {
                "label": result["label"],
                "packet_count": result["stats"]["packet_count"],
                "avg_packet_size": result["stats"]["avg_packet_size"],
                "unique_src_ips": result["stats"]["unique_src_ips"],
                "unique_dst_ips": result["stats"]["unique_dst_ips"],
                "unique_dst_ports": result["stats"]["unique_dst_ports"],
                "tcp_count": result["stats"]["tcp_count"],
                "udp_count": result["stats"]["udp_count"],
                "reasons": "; ".join(result["reasons"]),
            }

            save_result_to_csv("results/detection_results.csv", row)


def start_sniffing():
    print("Starting packet capture...")
    sniff(iface="en0", filter="ip", prn=process_packet, store=False)