environments = ["production", "testing"]
tools = ["docker", "jetking"]
print("---- starting multi-core infrastructure scanning ----")
for environment in environments:
    print(f"\n[connecting] connecting to {environment} section")
    for tool in tools:
        print(f" -> configuring {tool} for {environment} environment")