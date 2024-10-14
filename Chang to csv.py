import csv
import json

# Function to convert the 'safe_network_health' structure to CSV
def convert_safe_network_health_to_csv(json_file_path, csv_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        network_data = data['network_health']

        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            header = ['timestamp', 'source_port', 'destination_port', 'protocol', 'length', 
                      'traffic_direction', 'packet_rate', 'data_rate', 'is_encrypted', 
                      'destination_device', 'name', 'malicious', 'cpu_usage', 'memory_usage', 
                      'disk_usage', 'network_traffic_in', 'network_traffic_out', 'risk_score']
            writer.writerow(header)

            for record in network_data:
                writer.writerow([
                    record.get('timestamp', ''),
                    record.get('source_port', 0),
                    record.get('destination_port', 0),
                    record.get('protocol', ''),
                    record.get('length', 0),
                    record.get('traffic_direction', ''),
                    record.get('packet_rate', 0),
                    record.get('data_rate', 0),
                    record.get('is_encrypted', False),
                    record.get('destination_device', ''),
                    record.get('name', 0),
                    record.get('malicious', 0),
                    record.get('cpu_usage', 0),
                    record.get('memory_usage', 0),
                    record.get('disk_usage', 0),
                    record.get('network_traffic_in', 0),
                    record.get('network_traffic_out', 0),
                    record.get('risk_score', 0)
                ])

# Function to convert the 'attack_network_health' structure to CSV
def convert_attack_network_health_to_csv(json_file_path, csv_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            header = ['timestamp', 'source_port', 'destination_port', 'protocol', 'length', 
                      'traffic_direction', 'packet_rate', 'data_rate', 'is_encrypted', 
                      'destination_device', 'name', 'malicious', 'cpu_usage', 'memory_usage', 
                      'disk_usage', 'network_traffic_in', 'network_traffic_out', 'risk_score']
            writer.writerow(header)

            for record in data:
                writer.writerow([
                    record.get('timestamp', ''),
                    record.get('source_port', 0),
                    record.get('destination_port', 0),
                    record.get('protocol', ''),
                    record.get('length', 0),
                    record.get('traffic_direction', ''),
                    record.get('packet_rate', 0),
                    record.get('data_rate', 0),
                    record.get('is_encrypted', False),
                    record.get('destination_device', ''),
                    record.get('name', 0),
                    record.get('malicious', 0),
                    record.get('cpu_usage', 0),
                    record.get('memory_usage', 0),
                    record.get('disk_usage', 0),
                    record.get('network_traffic_in', 0),
                    record.get('network_traffic_out', 0),
                    record.get('risk_score', 0)
                ])

# Convert the JSON files to CSV
convert_safe_network_health_to_csv('safe_network_health_20000.json', 'safe_network_health_20000.csv')
convert_attack_network_health_to_csv('attack_network_health_20000.json', 'attack_network_health_20000.csv')

print("Conversion completed successfully.")

