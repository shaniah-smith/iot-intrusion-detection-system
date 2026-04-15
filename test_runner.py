from traffic_simulator import (
    simulate_normal_traffic,
    simulate_dos_traffic,
    simulate_port_scan,
)

TARGET_IP = "192.168.1.170"   


if __name__ == "__main__":
    print("Choose a test:")
    print("1 = Normal Traffic")
    print("2 = DoS Traffic")
    print("3 = Port Scan")

    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        simulate_normal_traffic(TARGET_IP, duration=15)
    elif choice == "2":
        simulate_dos_traffic(TARGET_IP, duration=5)
    elif choice == "3":
        simulate_port_scan(TARGET_IP)
    else:
        print("Invalid choice.")