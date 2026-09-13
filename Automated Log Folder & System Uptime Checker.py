import os
import subprocess

log_folder = "server_log"

if not os.path.exists(log_folder):
    os.makedirs(log_folder)
    print(f"step1 '{log_folder}' is not exists! but now added")

else:
    print(f"step1 '{log_folder}' is already exists")


try:
    print("step2 System uptime is ongoing")


    result = subprocess.run(["hostname"], capture_output=True, text=True, check=True)
    print("system status output:")
    print(result.stdout)

except FileNotFoundError:
    print("error:command is not found in system")
except subprocess.CalledProcessError:
    print("error:command is not execute")