#Program to archieve old log files 

import os
import shutil
from datetime import datetime

def archieve_logs(log_dir, archive_dir):
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

#Create files in the Directory
    for i in range(1,10,2):
        filename = f"ERROR_{i}_01_2025.log"
        filepath = os.path.join(log_dir,filename)
        with open(filepath,"w") as file:
            file.write("File created")
        print(f"Created : {filename}")

#Archieve the files ending with 01_2025.log 
    for log_file in os.listdir(log_dir):
        if log_file.endswith("01_2025.log"):
           new_name = f"{log_file}.gz"
           print(f"Archived {log_file} to {new_name}")

           shutil.move(
               os.path.join(log_dir, log_file),
               os.path.join(archive_dir,new_name)
           )
          

archieve_logs("logs_dir", "Archived_Dir")


