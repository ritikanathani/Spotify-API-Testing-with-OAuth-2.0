import pytest
from utils.helpers import make_request

BASE_URL = "https://api.spotify.com/v1"

def test_invalid_endpoint():
    endpoint = f"{BASE_URL}/invalid-endpoint"
    response = make_request(endpoint)
    assert response.status_code == 404

def test_invalid_method():
    endpoint = f"{BASE_URL}/browse/new-releases"
    import pytest
    from utils.helpers import make_request
    with pytest.raises(ValueError):
        make_request(endpoint, method="DELETE")
