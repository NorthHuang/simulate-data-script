import random
import json
from datetime import datetime, timedelta

# Function to calculate risk score for attack scenarios
def calculate_risk_score(cpu_usage, memory_usage, disk_usage, network_traffic_in, network_traffic_out):
    # CPU usage score
    if cpu_usage < 10:
        cpu_score = 0
    elif 10 <= cpu_usage < 20:
        cpu_score = 1
    elif 20 <= cpu_usage < 30:
        cpu_score = 2
    elif 30 <= cpu_usage < 40:
        cpu_score = 3
    elif 40 <= cpu_usage < 50:
        cpu_score = 4
    elif 50 <= cpu_usage < 60:
        cpu_score = 5
    elif 60 <= cpu_usage < 70:
        cpu_score = 6
    elif 70 <= cpu_usage < 80:
        cpu_score = 7
    elif 80 <= cpu_usage < 90:
        cpu_score = 8
    else:
        cpu_score = 9

    # Memory usage score
    if memory_usage < 10:
        memory_score = 0
    elif 10 <= memory_usage < 20:
        memory_score = 1
    elif 20 <= memory_usage < 30:
        memory_score = 2
    elif 30 <= memory_usage < 40:
        memory_score = 3
    elif 40 <= memory_usage < 50:
        memory_score = 4
    elif 50 <= memory_usage < 60:
        memory_score = 5
    elif 60 <= memory_usage < 70:
        memory_score = 6
    elif 70 <= memory_usage < 80:
        memory_score = 7
    elif 80 <= memory_usage < 90:
        memory_score = 8
    else:
        memory_score = 9

    # Disk usage score
    if disk_usage < 10:
        disk_score = 0
    elif 10 <= disk_usage < 20:
        disk_score = 1
    elif 20 <= disk_usage < 30:
        disk_score = 2
    elif 30 <= disk_usage < 40:
        disk_score = 3
    elif 40 <= disk_usage < 50:
        disk_score = 4
    elif 50 <= disk_usage < 60:
        disk_score = 5
    elif 60 <= disk_usage < 70:
        disk_score = 6
    elif 70 <= disk_usage < 80:
        disk_score = 7
    elif 80 <= disk_usage < 90:
        disk_score = 8
    else:
        disk_score = 9

    # Inbound traffic score
    if network_traffic_in < 100:
        traffic_in_score = 0
    elif 100 <= network_traffic_in < 200:
        traffic_in_score = 1
    elif 200 <= network_traffic_in < 400:
        traffic_in_score = 2
    elif 400 <= network_traffic_in < 600:
        traffic_in_score = 3
    elif 600 <= network_traffic_in < 800:
        traffic_in_score = 4
    elif 800 <= network_traffic_in < 1000:
        traffic_in_score = 5
    elif 1000 <= network_traffic_in < 1500:
        traffic_in_score = 6
    elif 1500 <= network_traffic_in < 2000:
        traffic_in_score = 7
    elif 2000 <= network_traffic_in < 3000:
        traffic_in_score = 8
    else:
        traffic_in_score = 9

    # Outbound traffic score
    if network_traffic_out < 100:
        traffic_out_score = 0
    elif 100 <= network_traffic_out < 200:
        traffic_out_score = 1
    elif 200 <= network_traffic_out < 400:
        traffic_out_score = 2
    elif 400 <= network_traffic_out < 600:
        traffic_out_score = 3
    elif 600 <= network_traffic_out < 800:
        traffic_out_score = 4
    elif 800 <= network_traffic_out < 1000:
        traffic_out_score = 5
    elif 1000 <= network_traffic_out < 1500:
        traffic_out_score = 6
    elif 1500 <= network_traffic_out < 2000:
        traffic_out_score = 7
    elif 2000 <= network_traffic_out < 3000:
        traffic_out_score = 8
    else:
        traffic_out_score = 9

    # Calculate total risk score based on weights
    risk_score = (0.25 * cpu_score) + (0.2 * memory_score) + (0.1 * disk_score) + (0.2 * traffic_in_score) + (0.2 * traffic_out_score)
    return round(risk_score, 2)

# Function to generate attack data with attack-specific characteristics
def generate_attack_data(attack_type, num_records):
    data = []
    start_time = datetime(2024, 8, 26, 12, 0, 0)

    for _ in range(num_records):
        timestamp = start_time + timedelta(seconds=random.randint(1, 600))

        if attack_type == 'DDoS':
            # DDoS attack characteristics
            cpu_usage = round(random.uniform(70, 100), 2)
            memory_usage = round(random.uniform(70, 100), 2)
            disk_usage = round(random.uniform(70.0, 100.0), 2)
            network_traffic_in = random.randint(2000, 5000)  # Very high
            network_traffic_out = random.randint(2000, 5000)  # High data rate
        elif attack_type == 'MITM':
            # MITM attack characteristics
            cpu_usage = round(random.uniform(50, 70), 2)
            memory_usage = round(random.uniform(50, 70), 2)
            disk_usage = round(random.uniform(55.0, 80.0), 2)
            network_traffic_in = random.randint(500, 1000)  # Moderate traffic
            network_traffic_out = random.randint(400, 1000)  # Irregular traffic
        elif attack_type == 'SQL Injection':
            # SQL Injection attack characteristics
            cpu_usage = round(random.uniform(60, 95), 2)
            memory_usage = round(random.uniform(60, 95), 2)
            disk_usage = round(random.uniform(70.0, 100.0), 2)
            network_traffic_in = random.randint(400, 1000)  # Low to moderate packet rate
            network_traffic_out = random.randint(2000, 5000)  # High data extraction rate
        elif attack_type == 'Phishing':
            # Phishing attack characteristics
            cpu_usage = round(random.uniform(40, 70), 2)
            memory_usage = round(random.uniform(40, 70), 2)
            disk_usage = round(random.uniform(50.0, 100.0), 2)
            network_traffic_in = random.randint(300, 800)  # Moderate traffic
            network_traffic_out = random.randint(400, 1000)  # Moderate outbound traffic

        # Network traffic metadata
        source_port = random.randint(1024, 65535)
        destination_port = random.randint(1024, 65535)
        protocol = random.choice(["TCP", "UDP"])
        length = random.randint(500, 2000)
        traffic_direction = random.choice(["inbound", "outbound"])
        packet_rate = random.randint(100, 500)
        data_rate = random.randint(100000, 500000)
        is_encrypted = random.choice([True, False])
        destination_device = random.choice(["Linux server", "Windows server"])

        # Calculate risk score
        risk_score = calculate_risk_score(cpu_usage, memory_usage, disk_usage, network_traffic_in, network_traffic_out)

        # Generate attack entry with specific name for attack type
        entry = {
            "timestamp": timestamp.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "source_port": source_port,
            "destination_port": destination_port,
            "protocol": protocol,
            "length": length,
            "traffic_direction": traffic_direction,
            "packet_rate": packet_rate,
            "data_rate": data_rate,
            "is_encrypted": is_encrypted,
            "destination_device": destination_device,
            "name": attack_type,  # Attack type as the name
            "malicious": "1",  # Malicious data
            "cpu_usage": cpu_usage,
            "memory_usage": memory_usage,
            "disk_usage": disk_usage,
            "network_traffic_in": network_traffic_in,
            "network_traffic_out": network_traffic_out,
            "risk_score": risk_score
        }
        data.append(entry)
    
    return data

# Function to generate 20,000 attack records (5000 per attack type)
def generate_attack_dataset(num_total_records=20000):
    attack_types = ["DDoS", "MITM", "SQL Injection", "Phishing"]
    num_records_per_attack = num_total_records // len(attack_types)
    dataset = []

    # Generate 5000 records for each attack type
    for attack_type in attack_types:
        dataset += generate_attack_data(attack_type, num_records_per_attack)
    
    return dataset

# Generate the dataset
attack_data = generate_attack_dataset()

# Save the dataset to a JSON file
output_file = 'attack_network_health_20000.json'
with open(output_file, 'w') as f:
    json.dump(attack_data, f, indent=4)

print(f"Attack data saved to {output_file}")