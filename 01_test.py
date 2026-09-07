name = input("enter your name: ")

age = int(input("enter your age: "))

if age >= 18:
    print(f"Hey {name}, you are eligible for big tech internships!")
else:
    print(f"Hey {name}, you are {age} and not legally ready for big tech internships ")
if age <= 15:
    print(f"hey {name},you are only {age} so focus on your studies first")
