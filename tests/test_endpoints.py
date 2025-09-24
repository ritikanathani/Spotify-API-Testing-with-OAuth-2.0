from utils.helpers import make_request

BASE_URL = "https://api.spotify.com/v1"

def test_get_new_releases():
    endpoint = f"{BASE_URL}/browse/new-releases"
    response = make_request(endpoint)
    assert response.status_code == 200
    data = response.json()
    assert "albums" in data

def test_get_featured_playlists():
    endpoint = f"{BASE_URL}/browse/featured-playlists"
    response = make_request(endpoint)
    assert response.status_code == 200
    data = response.json()
    assert "playlists" in data
