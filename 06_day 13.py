servers = ["aws-web-prod", "azure-db-secure", "gcp-api-gateway"]

print("--- Step 1: Deploying a New Infrastructure ---")
servers.append(new_node)

print("\n--- Step 2: Starting Automation Scan ---")
print("Scanning all deployed systems...\n")
for server in servers:
    print(f"[STATUS: ONLINE] Monitoring active on server: {server}")

print("\n--- Scan Completed Successfully ---")
