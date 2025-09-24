from utils.helpers import get_access_token

def test_token_generation():
    token = get_access_token()
    assert token is not None
    assert isinstance(token, str)
    assert len(token) > 0
