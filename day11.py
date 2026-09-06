skip_number = int(input("which number you want to skip??(1-10): "))
print(f"\n---dynamic loop start (skipping {skip_number})---")
i = 0
while i < 10:
    i = i + 1
    if i == skip_number:
        print(f"number({i}) found! skipping this step")
        continue
    print("number:", i)
