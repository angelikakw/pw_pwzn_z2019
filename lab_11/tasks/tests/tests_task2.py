import json
from unittest.mock import Mock, patch
from urllib.parse import urljoin

import pytest
import requests
import requests_mock

from lab_11.tasks.tools.metaweather import (
    get_metaweather,
    get_cities_woeid
)

API_URL = 'https://www.metaweather.com/api/'


def test_war():
    with requests_mock.Mocker() as m:
        location_url = urljoin(API_URL, 'location/search')

        m.get(location_url, text='[{"title":"Warsaw","location_type":"City","woeid":523920,"latt_long":"52.235352,21.009390"}'
                                 ',{"title":"Newark","location_type":"City","woeid":2459269,"latt_long":"40.731972,-74.174179"}]'
              , status_code=200)

        assert get_cities_woeid('War') == {
        'Warsaw': 523920,
        'Newark': 2459269,
    }


def test_warszawa():
    with requests_mock.Mocker() as m:
        location_url = urljoin(API_URL, 'location/search')

        m.get(location_url, text='{}', status_code=200)
        assert get_cities_woeid('Warszawa') == {}


def test_timeout():
    try:
        with requests_mock.Mocker() as m:
            location_url = urljoin(API_URL, 'location/search')
            m.get(location_url, exc=requests.exceptions.Timeout)
            get_cities_woeid('Warsaw', 5.)
    except Exception as exc:
        assert isinstance(exc, requests.exceptions.Timeout)
