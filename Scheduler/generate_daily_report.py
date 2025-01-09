import psutil
import os
from datetime import datetime


#Generate daily report
def generate_daily_report():
    print(f"[{datetime.now()}] Generating daily report...")
   
    # Get the current date and time
    current_time = datetime.now()
    report_date = current_time.strftime("%Y-%m-%d")
    print("Report_Date : ", report_date)
    report_time = current_time.strftime("%H_%M_%S")
    print("Report_Time : ", report_time)

    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')

    # Create the report content
    report_content = f"""
    Daily Report - {report_date}
    Time Generated: {report_time}

    System Information:
    -------------------
    CPU Usage: {cpu_usage}%
    Memory Usage: {memory_info.percent}%
    Disk Usage: {disk_usage.percent}%
        
    """
     # Define the report file name and save location
    report_dir = r"../Python/Scheduler/Source/Daily_reports"
    if not os.path.exists(report_dir):
        os.makedirs(report_dir) 

    report_file = os.path.join(report_dir, f"daily_report_{report_date}_{report_time}.txt")
    print("Report File : ", report_file)

    # Write the report to a file
    with open(report_file, 'w') as file:
         file.write(report_content)

    print(f"Daily report generated successfully: {report_file}")
