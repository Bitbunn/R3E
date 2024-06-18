# monitor.py
from shared_memory_reader import SharedMemoryReader
import time

def monitor_values():
    reader = SharedMemoryReader()
    while True:
        data = reader.get_player_data()
        if data:
            print("Position:", data.get('Position', 'N/A'))
            print("Velocity:", data.get('Velocity', 'N/A'))
            print("SuspensionDeflection:", data.get('SuspensionDeflection', 'N/A'))
            print("WheelSlip:", data.get('WheelSlip', 'N/A'))
            print("TireLoad:", data.get('TireLoad', 'N/A'))
        else:
            print("Failed to retrieve data. Data is None.")
        time.sleep(0.5)

if __name__ == "__main__":
    monitor_values()
