#This script checks server CPU, memory and disk usage

import psutil

def check_server_health():
    #CPU Usage
    cpu = psutil.cpu_percent(interval=1)
    print(f"CPU Usage : {cpu}%")

    #Memory
    memory = psutil.virtual_memory()
    mem = psutil.swap_memory()
    print(f"Swap Memory : {mem.percent}%")
    print(f"Virtual Memory : {memory.percent}%")

    #hard-disk
    disk = psutil.disk_usage("/")
    print(f"Hard Disk Usage : {disk.percent}%")

    if any([cpu > 80, memory.percent > 80 , disk.percent >80]):
        print("Warning : Resource usage exceeds thresold")


check_server_health()
