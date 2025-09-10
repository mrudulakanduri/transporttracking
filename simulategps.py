import requests
import time
import random

vehicle_ids = ['BUS1', 'VAN2']
base_lat = 28.6139
base_lon = 77.2090

while True:
    for vehicle_id in vehicle_ids:
        data = {
            "vehicle_id": vehicle_id,
            "latitude": base_lat + random.uniform(-0.01, 0.01),
            "longitude": base_lon + random.uniform(-0.01, 0.01)
        }
        try:
            response = requests.post('http://127.0.0.1:5000/update-location', json=data)
            print(f"Sent data for {vehicle_id}: {response.status_code}")
        except Exception as e:
            print(f"Error sending data: {e}")
    time.sleep(5)
