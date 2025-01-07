import psutil
import time
import logging

# Configuration
CPU_THRESHOLD = 90  # in percentage
MEMORY_THRESHOLD = 90  # in percentage
DISK_THRESHOLD = 90  # in percentage
LOG_FILE = "resource_monitor.log"
CHECK_INTERVAL = 5  # in seconds

# Setup logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Function to check resource usage
def check_resources():
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage: {cpu_usage}%")
        print(f"High CPU usage: {cpu_usage}%")

    # Check memory usage
    memory = psutil.virtual_memory()
    if memory.percent > MEMORY_THRESHOLD:
        logging.warning(f"High memory usage: {memory.percent}%")
        print(f"High memory usage: {memory.percent}%")

    # Check disk usage
    disk = psutil.disk_usage("/")
    if disk.percent > DISK_THRESHOLD:
        logging.warning(f"High disk usage: {disk.percent}%")
        print(f"High disk usage: {disk.percent}%")

# Main monitoring loop
def monitor_resources():
    print("Starting resource monitoring...")
    while True:
        check_resources()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    try:
        monitor_resources()
    except KeyboardInterrupt:
        print("Monitoring stopped.")
