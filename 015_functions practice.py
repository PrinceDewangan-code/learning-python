def send_server_alert(server_name, status):
    if status.lower() == "running":
        print(f"[INFO] Server '{server_name}' is UP and HEALTHY! 🟢")
    elif status.lower() == "stopped":
        print(f"[WARNING] Server '{server_name}' is DOWN! 🔴")
    else:
        print(f"[UNKNOWN] Server '{server_name}' status is UNKNOWN! 🟡")

name = input ("Enter Server Name:")
stat = input ("enter server status (running/stopped)")

send_server_alert(name ,stat)

