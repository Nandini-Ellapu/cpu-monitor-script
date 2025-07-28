# CPU Monitor Script (Python)

This Python script uses the `psutil` library to monitor:

- ✅ Total CPU usage percentage
- ✅ Per-core CPU usage
- ✅ CPU frequency (in MHz)

## 🔧 Requirements

- Python 3.x
- psutil

# Step 1: Install Required Library
✅ What is psutil?

psutil (Python system and process utilities) is a library that gives you access to information about CPU, memory, disks, sensors, and running processes.
🔧 Install it
# Open a terminal or command prompt and type:
pip install psutil

✅ This command will download and install psutil.
# Step 2: Import the Library in Your Script
Create a Python file like cpu_monitor.py and start by importing the required libraries:

import psutil

import time
✅ psutil: Used for system information

✅ time: Used to pause between readings
# Step 3: Create and Run a Python Script
Instead of running Python line-by-line in the terminal, create a file cpu_monitor.py and paste the following code:

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
# Step 4: Run the Python File from Command Prompt

From the directory where the script is saved, run: python cpu_monitor.py

✅ Output will show CPU usage updates every few seconds.



