import requests

from config import AIRTABLE_API_KEY, AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME

session = requests.Session()  # using one session to increase efficiency
session.headers.update({'Authorization': f'Bearer {AIRTABLE_API_KEY}', 'Content-Type': 'application/json'})


def save_movie_data(movie_data):
    url = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'
    data = {
        'fields': {
            'Название': movie_data['Title'],
            'Режиссер': movie_data['Director'],
            'Сценарист': movie_data['Writer'],
            'Дата выхода': movie_data['Released'],
            'Краткий сюжет': movie_data['Plot'],
            'Обложка': movie_data['Poster']
        }
    }
    try:
        response = session.post(url, json=data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'Error saving movie {movie_data["Title"]}: {e}')
