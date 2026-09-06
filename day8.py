number= int(input("enter a number to print its table:"))
print (f"\n--- table of {number} using loop ---")
for i in range(1, 11):
    result= number * i
    print(f"{number} x {i} = {result}")
