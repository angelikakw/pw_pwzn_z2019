import pytest
import requests
import requests_mock

from lab_11.tasks.tools.metaweather import (
    get_metaweather,
    get_cities_woeid
)


