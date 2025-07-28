import psutil
import time

while True:
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_freq = psutil.cpu_freq()
    per_core_usage = psutil.cpu_percent(interval=1, percpu=True)

    print(f"Total CPU Usage: {cpu_percent}%")
    print(f"CPU Frequency: {cpu_freq.current:.2f} MHz")
    print("Per-Core CPU Usage:", per_core_usage)
    print("-" * 40)

    time.sleep(2)
