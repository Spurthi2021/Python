#Cron job to run the script in every mentioned interval

def create_cron_job(cmd, schedule, user):
    cron_job = f"{schedule} {cmd}\n"
    cron_file = f"cron/{user}"

    with open(cron_file, "a") as f:
        f.write(cron_job)
    print(f"Cron Job added : {cron_job.strip()}")

#Run every midnight @ 12
create_cron_job(r"\Users\spuhi\Python\Average.py", "0 0 * * *", "root")
