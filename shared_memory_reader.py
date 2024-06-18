# shared_memory_reader.py
from r3e_api import R3ESharedMemory
import time

class SharedMemoryReader:
    def __init__(self):
        self.shared_memory = R3ESharedMemory()
        self.shared_memory.update_offsets()  # Only needed once

    def get_player_data(self):
        self.shared_memory.update_buffer()
        return self.shared_memory.get_value('Player')

if __name__ == "__main__":
    reader = SharedMemoryReader()
    while True:
        data = reader.get_player_data()
        print(data)
        time.sleep(0.5)
