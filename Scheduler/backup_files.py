#Backup files
import os
import shutil
import psutil
from datetime import datetime

def backup_files():
    print(f"[{datetime.now()}] Backing up files...")
    # Example backup logic
    source_dir = "C:/Users/spuhi/Python/Source/Daily_reports"  
    backup_dir = "C:/Users/spuhi/Python/backUp"  
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    for filename in os.listdir(source_dir):
        full_file_name = os.path.join(source_dir, filename)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, backup_dir)