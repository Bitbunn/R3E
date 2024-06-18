# visualize.py
from shared_memory_reader import SharedMemoryReader
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# Initialize shared memory reader
reader = SharedMemoryReader()

# Lists to store data for plotting
times = []
speeds = []

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Initialize the line for speed
line, = ax.plot([], [], label="Speed (m/s)")

# Configure the speed plot
ax.set_xlim(0, 10)
ax.set_ylim(0, 300)  # Adjust based on expected speed range
ax.set_xlabel("Time (s)")
ax.set_ylabel("Speed (m/s)")
ax.legend()

# Function to initialize the plot
def init():
    line.set_data([], [])
    return line,

# Function to update the plot
def update(frame):
    data = reader.get_player_data()

    if data:
        current_time = time.time() - start_time
        try:
            speed = data['Speed']  # Example, replace with actual key
        except KeyError:
            print("Key 'Speed' not found in the data. Available keys:", data.keys())
            return line,

        times.append(current_time)
        speeds.append(speed)

        # Keep only the last 100 data points for a smooth real-time graph
        times_trimmed = times[-100:]
        speeds_trimmed = speeds[-100:]

        line.set_data(times_trimmed, speeds_trimmed)

        ax.set_xlim(times_trimmed[0], times_trimmed[-1])
        ax.set_ylim(0, max(speeds_trimmed) + 5)  # Ensure Y-axis starts at 0
    return line,

# Capture the start time
start_time = time.time()

# Create an animation that updates the plot
ani = FuncAnimation(fig, update, init_func=init, blit=True, interval=100)  # Interval is in milliseconds

plt.tight_layout()
plt.show()
