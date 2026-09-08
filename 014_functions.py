def check_status(server_name,status):
    print (f"---AUDITING {server_name}---")
    if status.lower() == "active":
        print (f"===> Server {server_name} is running smoothly <===")

    else:
        print (f"===> Alert server {server_name} is down! <===")

print("---AUTOMATION IS STARTS FROM NOW!---")

check_status("server1","active")
check_status("server2","inactive")
check_status("server3","active")