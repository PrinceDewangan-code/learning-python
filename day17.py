movies = []
print ("\n---ADDING MOVIES---")

movie1 = input("\nenter the name of movie1: ")
movies.append(movie1)

movie2 = input("enter the name of movie2: ")
movies.append(movie2)

movie3 = input("enter the name of movie3: ")
movies.append(movie3)

correct_password = "tag"

attempts = 0
max_attempts = 3
access_granted = False

print ("\n---PASSWORD REQUIRED---")

while attempts < max_attempts:
    password = input("enter password: ")

    if password == correct_password:
        access_granted = True
        break
    else:
        attempts = attempts + 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print("\nIncorrect password you have" , remaining_attempts, "attempts left")


if access_granted == True:
    print("\nACCESS GRANTED")
    for movie in movies:
        print("movie saved:", movie)

else:
    print("\nACCESS DENIED  ")

