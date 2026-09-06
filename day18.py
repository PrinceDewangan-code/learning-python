server = {}

print("---creation panel---")

server["name"] = input("enter the name of server:")
server["ip"] = input("enter the ip of server:")
server["environment"] = input("enter the environment of server:")

print("\n---server details---")
for key, value in server.items():
    print(f"server {key}: {value}")
print(f"\n full server details:{server}")
