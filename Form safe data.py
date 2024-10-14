import random
import json
from datetime import datetime, timedelta

# Function to calculate risk score for normal network operation
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
    else:
        cpu_score = 4  # Cap for normal data

    # Memory usage score
    if memory_usage < 10:
        memory_score = 0
    elif 10 <= memory_usage < 20:
        memory_score = 1
    elif 20 <= memory_usage < 30:
        memory_score = 2
    elif 30 <= memory_usage < 40:
        memory_score = 3
    else:
        memory_score = 4  # Cap for normal data

    # Disk usage score
    if disk_usage < 10:
        disk_score = 0
    elif 10 <= disk_usage < 20:
        disk_score = 1
    elif 20 <= disk_usage < 30:
        disk_score = 2
    elif 30 <= disk_usage < 40:
        disk_score = 3
    else:
        disk_score = 4  # Cap for normal data

    # Inbound traffic score
    if network_traffic_in < 100:
        traffic_in_score = 0
    elif 100 <= network_traffic_in < 200:
        traffic_in_score = 1
    elif 200 <= network_traffic_in < 400:
        traffic_in_score = 2
    else:
        traffic_in_score = 3  # Cap for normal data

    # Outbound traffic score
    if network_traffic_out < 100:
        traffic_out_score = 0
    elif 100 <= network_traffic_out < 200:
        traffic_out_score = 1
    elif 200 <= network_traffic_out < 400:
        traffic_out_score = 2
    else:
        traffic_out_score = 3  # Cap for normal data

    # Calculate total risk score
    risk_score = (0.25 * cpu_score) + (0.2 * memory_score) + (0.1 * disk_score) + (0.2 * traffic_in_score) + (0.2 * traffic_out_score)
    return min(round(risk_score, 2), 3)

# Function to generate normal network operation data with randomized network traffic information
def generate_safe_data(num_records=20000):
    data = []
    start_time = datetime(2024, 8, 26, 12, 0, 0)

    for _ in range(num_records):
        # Generate timestamp incrementally
        timestamp = start_time + timedelta(seconds=random.randint(1, 600))

        # Normal operation characteristics for network traffic
        source_port = random.randint(1024, 65535)
        destination_port = random.randint(1024, 65535)
        protocol = random.choice(["TCP", "UDP"])
        length = random.randint(500, 2000)
        traffic_direction = random.choice(["inbound", "outbound"])
        packet_rate = random.randint(50, 300)
        data_rate = random.randint(10000, 100000)
        is_encrypted = random.choice([True, False])
        destination_device = random.choice(["Linux server", "Windows server"])

        # Normal operation characteristics for system health
        cpu_usage = round(random.uniform(5, 40), 2)
        memory_usage = round(random.uniform(5, 50), 2)
        disk_usage = round(random.uniform(5, 50), 2)
        network_traffic_in = random.randint(50, 400)  # Normal traffic in
        network_traffic_out = random.randint(50, 400)  # Normal traffic out
        
        # Calculate a lower risk score for normal data
        risk_score = calculate_risk_score(cpu_usage, memory_usage, disk_usage, network_traffic_in, network_traffic_out)

        # Entry structure with "safe" type and "malicious" = 0
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
            "name": 0,  # Safe data
            "malicious": "0",  # Safe data
            "cpu_usage": cpu_usage,
            "memory_usage": memory_usage,
            "disk_usage": disk_usage,
            "network_traffic_in": network_traffic_in,
            "network_traffic_out": network_traffic_out,
            "risk_score": risk_score
        }

        data.append(entry)
    
    return data

# Generate the safe dataset
safe_data = generate_safe_data()

# Save the dataset to a JSON file
output_file = 'safe_network_health_20000.json'
with open(output_file, 'w') as f:
    json.dump({"network_health": safe_data}, f, indent=4)

print(f"Safe network health data saved to {output_file}")
