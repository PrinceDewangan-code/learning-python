target_pin = int(input("Enter a 4-digit secret PIN to hide: "))
print(f"\n--- Starting Password Cracker for PIN: {target_pin} ---")
i = 0
while i <=9999:
    if i == target_pin:
        print(f"[SUCCESS] Password Cracked!: {i}")
        break
    print(f"[TRYING]: {i}")
    i = i + 1
