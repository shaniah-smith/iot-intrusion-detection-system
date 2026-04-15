from datetime import datetime, timedelta


class SimpleWindowDetector:
    def __init__(self, window_size=5):
        self.window_size = window_size
        self.window_start = datetime.now()
        self.packet_features = []

    def add_packet(self, feature):
        self.packet_features.append(feature)
        now = datetime.now()

        if now - self.window_start >= timedelta(seconds=self.window_size):
            stats = self.compute_window_stats()
            self.window_start = now
            self.packet_features = []
            return stats

        return None

    def compute_window_stats(self):
        if not self.packet_features:
            return None

        packet_count = len(self.packet_features)
        avg_packet_size = sum(p["packet_size"] for p in self.packet_features) / packet_count
        unique_src_ips = len(set(p["src_ip"] for p in self.packet_features))
        unique_dst_ips = len(set(p["dst_ip"] for p in self.packet_features))
        unique_dst_ports = len(
            set(p["dst_port"] for p in self.packet_features if p["dst_port"] is not None)
        )
        tcp_count = sum(1 for p in self.packet_features if p["protocol"] == "TCP")
        udp_count = sum(1 for p in self.packet_features if p["protocol"] == "UDP")

        return {
            "packet_count": packet_count,
            "avg_packet_size": round(avg_packet_size, 2),
            "unique_src_ips": unique_src_ips,
            "unique_dst_ips": unique_dst_ips,
            "unique_dst_ports": unique_dst_ports,
            "tcp_count": tcp_count,
            "udp_count": udp_count,
        }


class RuleBasedIDS:
    def detect(self, stats):
        if stats is None:
            return None

        reasons = []

        if stats["packet_count"] > 60:
            reasons.append("Possible DoS: high packet volume")

        if stats["unique_dst_ports"] > 8:
            reasons.append("Possible Port Scan: many destination ports targeted")

        if stats["avg_packet_size"] < 120 and stats["packet_count"] > 50:
            reasons.append("Suspicious burst of small packets")

        if reasons:
            return {
                "label": "ALERT",
                "reasons": reasons,
                "stats": stats,
            }

        return {
            "label": "NORMAL",
            "reasons": [],
            "stats": stats,
        }