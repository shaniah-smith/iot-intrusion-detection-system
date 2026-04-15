# Lightweight Network Intrusion Detection System for IoT Environments

## Author
Shaniah Smith  
Howard University, Computer Science Major, Mathematics Minor

## Overview
This project implements a lightweight Network Intrusion Detection System (NIDS) for IoT and Cyber-Physical System (CPS) environments. The system captures live network traffic, extracts packet-level features, aggregates traffic into time windows, and applies rule-based anomaly detection to identify suspicious behavior such as denial-of-service (DoS) traffic and port scanning.

## Motivation
Traditional intrusion detection systems can be too resource-intensive for IoT environments. This project explores a lightweight, Python-based alternative that can monitor traffic in near real time using packet sniffing and simple statistical rules.

## Features
- Real-time packet capture using Scapy
- Packet feature extraction:
  - source IP
  - destination IP
  - source port
  - destination port
  - protocol
  - packet size
  - timestamp
- 5-second traffic window aggregation
- Rule-based intrusion detection
- Detection of:
  - DoS-like traffic
  - port scanning
  - abnormal bursts of small packets
- CSV logging of detection windows
- Graph generation for evaluation

## Project Files
- `main.py` — starts the IDS
- `sniffer.py` — packet capture and CSV logging
- `features.py` — packet feature extraction
- `detector.py` — windowing and rule-based IDS logic
- `traffic_simulator.py` — normal, DoS, and port-scan traffic generation
- `test_runner.py` — runs traffic simulations
- `analyze_results.py` — generates graphs from CSV data
- `evaluate.py` — computes simple experiment accuracy
- `utils.py` — helper functions for CSV output
- `requirements.txt` — Python dependencies

## Requirements
- Python 3
- Scapy
- pandas
- matplotlib
- scikit-learn

Install dependencies with:

```bash
python3 -m pip install -r requirements.txt
