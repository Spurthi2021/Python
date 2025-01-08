#Scheduling a Job to run a script every 10minutes

import schedule
import time
import subprocess

def run_script():
    try:
        print("Executing script...")
        subprocess.run(["python", "path/to/your/target_script.py"], check=True)
        print("Script executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

# Schedule the script to run every 10 minutes
schedule.every(10).minutes.do(run_script)

print("Scheduler started. The script will run every 10 minutes.")
while True:
    schedule.run_pending()
    time.sleep(1)
