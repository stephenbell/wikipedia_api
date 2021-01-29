import pytest

from src.wikipedia_api import client


@pytest.mark.parametrize("lang", [("en"), ("de"), ("fr")])
def test_random_page_uses_given_language(lang):
    json = client.get_random_summary_page_as_json(lang=lang)
    assert json["lang"] == lang
