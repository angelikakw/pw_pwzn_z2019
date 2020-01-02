import csv
import pathlib
from urllib.parse import urljoin
from typing import Optional, Union, List
from calendar import monthrange
from os.path import isdir, join
from os import makedirs, getcwd
import requests

API_URL = 'https://www.metaweather.com/api/'


def get_city_data(
        woeid: int, year: int, month: int,
        path: Optional[Union[str, pathlib.Path]] = None,
        timeout: float = 5.
) -> (str, List[str]):

    name_of_dir = '{}_{}_{:02}'.format(woeid, year, month)
    full_name_of_dir = join(path or getcwd(), name_of_dir)
    if not isdir(full_name_of_dir):
        makedirs(full_name_of_dir)

    days_in_month = monthrange(year, month)[1]
    all_files = []
    for day in range(1, days_in_month+1):

        location_url = urljoin(API_URL, f'location/{woeid}/{year}/{month}/{day}')
        records = make_request(location_url, timeout)
        if not records:
            continue

        name_of_file = '{}_{:02}_{:02}.csv'.format(year, month, day)
        all_files.append(name_of_file)
        full_name_of_file = join(full_name_of_dir, name_of_file)

        with open(full_name_of_file, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(records[0].keys())
            for row in records:
                writer.writerow(row.values())
    return full_name_of_dir, all_files


def make_request(location_url, timeout):
    response = requests.get(location_url, timeout=timeout)

    if response.status_code >= 400:
        raise requests.exceptions.HTTPError()

    try:
        response_json = response.json()
    except ValueError:
        raise RuntimeError('No valid json found.')

    return response_json


if __name__ == '__main__':
    _path = pathlib.Path.cwd()
    expected_path = _path / '523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3)
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert str(expected_path) == dir_path

    expected_path = 'weather_data/523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3, path='weather_data')
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path

    expected_path = 'weather_data/523920_2012_12'
    dir_path, file_paths = get_city_data(523920, 2012, 12, path='weather_data')
    assert len(file_paths) == 0
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path
