# Step 1: Khali list servers hold karne ke liye
servers = []

print("--- ENTER SERVER DETAILS ---")

# Step 2: Loop chala kar 2 servers ki detail le rahe hain
for i in range(1, 3):
    print(f"\nEnter Details for Server {i}:")
    
    server_info = {}
    server_info["name"] = input("Enter Server Name: ")
    server_info["ip"] = input("Enter Server IP: ")
    server_info["status"] = input("Enter status (active/inactive): ")
    
    # Dictionary ko main list mein append kar diya
    servers.append(server_info)

print("\n--- SECURITY CHECK ---")
# Step 3: Permission Trigger
trigger = input("Type 'audit' to run security health check: ")

# Step 4: Logic check (.lower() ke saath)
if trigger.lower() == "audit":
    print("\n--- RUNNING AUDIT REPORT ---")
    
    # List of Dictionaries par Loop
    for server in servers:
        # Dictionary ki 'status' key check kar rahe hain
        if server["status"].lower() == "active":
            print(f"🟢 [ONLINE] {server['name']} ({server['ip']}) - Security Check Passed!")
        else:
            print(f"🔴 [OFFLINE] {server['name']} ({server['ip']}) - Warning: Server is down!")

else:
    print("\nAudit cancelled by user.")