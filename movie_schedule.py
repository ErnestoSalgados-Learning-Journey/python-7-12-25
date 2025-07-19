current_movies = {'a bronx tail': '11:00am',
                  'the godfather': '1:00pm',
                  'coraline': '3:00pm',
                  'Lord of the Rings': '5:00pm',}

print("We're showing the following movies:")
for key in current_movies:
    print(key)

movie = input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie)

if showtime == None:
    print("We curently aren't playing that movie.")
else:
    print(movie, "is playing at", showtime)