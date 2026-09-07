favorite_movies = ["avengers","Ironman","Loki","doomsday","dr.strange"]
print ("\n--- current list of movies ---")
print (F"{favorite_movies}")
new_servers = input("\nenter the name of movie to add in the list: ")
favorite_movies.append(new_servers)
print ("\n--- updated list ---")
print (f"{favorite_movies}")
print ("\nif you want updating any server say 'yes' or 'no'")
if input() == "yes":
    choice =int(input("\nenter the index: "))
    print (f"{favorite_movies[choice]}")
    favorite_movies[choice] = input("\nenter the new name of movie:")
    print ("--- final list ---")
    print (f"{favorite_movies}")
else: 
    print ("no updates made")
    print ("--- final list ---")
    print (f"{favorite_movies}")