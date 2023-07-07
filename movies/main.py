from movies import movies, get_movie_data
from airtable_utils import save_movie_data

movies_data = []

for movie in movies:
    movie_data = get_movie_data(movie)
    if movie_data is not None:
        movies_data.append(movie_data)

for movie_data in movies_data:
    save_movie_data(movie_data)

print('Movie data saved to Airtable.')
