from unittest.mock import Mock, patch

import pytest
import requests
import requests_mock

from lab_11.tasks.tools.metaweather import (
    get_metaweather,
    get_cities_woeid
)

API_URL = 'https://www.metaweather.com/api/'


def test_url():
    with requests_mock.Mocker() as m:
        m.get(API_URL, text='resp')
        requests.get(API_URL).text

