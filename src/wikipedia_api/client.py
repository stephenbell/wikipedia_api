import requests


API_ENDPOINT = "https://{lang}.wikipedia.org/api/rest_v1/page/random/summary"


def get_random_summary_page_as_json(lang="en"):
    url = API_ENDPOINT.format(lang=lang)

    try:
        with requests.get(url) as response:
            response.raise_for_status()
            return response.json()
    except requests.RequestException as error:
        raise SystemExit(error)
