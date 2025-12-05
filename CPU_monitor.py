import psutil
import time

THRESHOLD = 80  # CPU usage threshold in percentage

print("Monitoring CPU usage... Press Ctrl+C to stop.")

try:
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"Current CPU Usage: {cpu_usage}%")
        if cpu_usage > THRESHOLD:
            print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")
except Exception as e:
    print(f"An error occurred: {e}")
