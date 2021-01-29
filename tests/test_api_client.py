from src.wikipedia_api import __version__
from src.wikipedia_api import client

import validators


def test_version():
    assert __version__ == "0.1.0"


def test_api_endpoint_is_valid_url():
    assert validators.url(str(client.API_ENDPOINT.format(lang="en")))


# def test_mock_req_get(mock_requests_get):
#    rsp = client.get_random_summary_page_as_json()
#    print(rsp)
