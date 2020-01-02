from urllib.parse import urljoin
import requests

API_URL = 'https://www.metaweather.com/api/'


def get_cities_woeid(query: str, timeout: float = 5.):
    location_url = urljoin(API_URL, 'location/search')
    response = requests.get(location_url, params=dict(query=query), timeout=timeout)

    if response.status_code >= 400:
        raise requests.exceptions.HTTPError()

    try:
        response_json = response.json()
    except ValueError:
        raise RuntimeError('No valid json found.')

    result = {}
    for record in response_json:
        if 'title' not in record or 'woeid' not in record:
            raise RuntimeError('No title or woeid.')
        result[record['title']] = record['woeid']

    return result


if __name__ == '__main__':
    assert get_cities_woeid('Warszawa') == {}
    assert get_cities_woeid('War') == {
        'Warsaw': 523920,
        'Newark': 2459269,
    }
    try:
        get_cities_woeid('Warszawa', 0.1)
    except Exception as exc:
        isinstance(exc, requests.exceptions.Timeout)
