import subprocess

def create_task(task_name, script_path, time="12:00"):
    try:
        command = f"schtasks /create /tn {task_name} /tr {script_path} /sc once /st {time}"
        subprocess.run(command, shell=True, check=True)
        print(f"Scheduled task '{task_name}' created.")
    except Exception as e:
        print(f"Failed to create scheduled task: {e}")

if __name__ == "__main__":
    create_task("DailyBackup", "C:/path/to/backup_script.py")
