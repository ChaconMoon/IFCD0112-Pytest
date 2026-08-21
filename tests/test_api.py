import requests

def test_rick_and_morty_api():
    url = "https://rickandmortyapi.com/api/"
    response = requests.get(url)
    
    assert response.status_code == 200