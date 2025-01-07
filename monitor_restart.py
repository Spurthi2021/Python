import subprocess
import time
import logging
import yaml
import psutil

# Load configuration from YAML file
def load_config(config_file="services_config.yaml"):
    with open(config_file, "r") as file:
        return yaml.safe_load(file)

# Setup logging
def setup_logging(log_file):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

# Check if a service is running
def is_service_running(service_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == service_name:
            return True
    return False

# Restart a service
def restart_service(service_name, restart_command):
    try:
        subprocess.run(restart_command, shell=True, check=True)
        logging.info(f"Successfully restarted service: {service_name}")
        print(f"Service {service_name} restarted successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to restart service: {service_name}. Error: {e}")
        print(f"Failed to restart service {service_name}.")

# Monitor services
def monitor_services(config):
    print("Starting service monitoring...")
    services = config['services']
    interval = config['check_interval']

    while True:
        for service in services:
            service_name = service['name']
            restart_command = service['restart_command']

            if not is_service_running(service_name):
                logging.warning(f"Service down: {service_name}")
                print(f"Service {service_name} is down. Attempting to restart...")
                restart_service(service_name, restart_command)
            else:
                logging.info(f"Service running: {service_name}")
                print(f"Service {service_name} is running normally.")

        time.sleep(interval)

if __name__ == "__main__":
    try:
        config = load_config("services_config.yaml")
        setup_logging(config['log_file'])
        monitor_services(config)
    except KeyboardInterrupt:
        print("Monitoring stopped.")
    except Exception as e:
        print(f"Error: {e}")
