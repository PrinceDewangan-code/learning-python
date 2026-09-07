server_list = []

print("--->MULTI SERVER MANAGER<---")

for i in range(1, 4):

    print(f"Enter the data for server {i}: ")

    user_info = {}
    user_info["name"] = input("\nEnter the server name: ")
    user_info["ip"] = input("Enter the server ip: ")
    user_info["environment"] = input("Enter the server environment: ")

    server_list.append(user_info)

print ("\n==================================================")
print("ALL REGISTERED SERVERS (DEPLOYMENT READINESS)")
print("==================================================")

for server in server_list:
    print(f"\nserver name: {server['name']}")
    print(f"server ip: {server['ip']}")
    print(f"server environment: {server['environment']}")