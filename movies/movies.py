import requests

from config import OMDB_API_KEY

session = requests.Session()  # using one session to increase efficiency

movies = [
    'Interstellar',
    'The Godfather',
    'Forrest Gump',
    'Fight Club',
    'Inception',
    'The Pianist',
    'Parasite',
    'Whiplash',
    'The Prestige',
    'The Shining'
]


def get_movie_data(movie):
    url = f'https://www.omdbapi.com/?t={movie}&apikey={OMDB_API_KEY}'
    try:
        response = session.get(url)
        response.raise_for_status()
        movie_data = response.json()
        return movie_data
    except requests.exceptions.RequestException as e:
        print(f'Error fetching movie data for {movie}: {e}')
        return None
