from generate_daily_report import generate_daily_report
from backup_files import backup_files
from datetime import datetime
import schedule
import os
import time

#Reminder
def daily_reminder():
    print(f"[{datetime.now()}] Reminder: Check for the reports and backup files in Generated today")

# Schedule tasks
#schedule.every().day.at("12:05").do(generate_daily_report)
schedule.every().minute.do(generate_daily_report)
schedule.every(2).minutes.do(backup_files)
#If for 1 minute then it would be 
#schedule.every(1).minute.do(backup_files)
schedule.every(2).hours.do(daily_reminder)

# Main loop
if __name__ == "__main__":
    print("Task Scheduler Started...")
    while True:
        schedule.run_pending()
        time.sleep(1)
