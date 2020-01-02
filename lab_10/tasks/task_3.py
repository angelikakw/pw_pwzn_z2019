import filecmp
import pathlib
from glob import glob
from os.path import join
from typing import Union

import pandas as pd


API_URL = 'https://www.metaweather.com/api/'


def concat_data(
        path: Union[str, pathlib.Path],
):
    all_necessary_data = []
    for file_path in glob(join(path, '*.csv')):
        data_in_file = pd.read_csv(file_path)
        filter_data = pd.to_datetime(data_in_file['created']).dt.date == \
                   pd.to_datetime(data_in_file['applicable_date']).dt.date
        all_necessary_data.append(data_in_file[filter_data])
    all_data_concat = pd.concat(all_necessary_data)
    all_data_concat.rename(columns={'the_temp': 'temp'}, inplace=True)
    selected_columns = pd.DataFrame(all_data_concat,
                             columns=['created', 'min_temp', 'temp', 'max_temp',
                                      'air_pressure', 'humidity', 'visibility',
                                      'wind_direction_compass', 'wind_direction',
                                      'wind_speed'])
    selected_columns.sort_values(['created'], inplace=True)
    selected_columns['created'] = pd.to_datetime(selected_columns['created']).dt.strftime('%Y-%m-%dT%H:%M')
    selected_columns.to_csv('{}.csv'.format(path), index=False)


if __name__ == '__main__':
    concat_data('weather_data/523920_2017_03')
    assert filecmp.cmp(
        'expected_523920_2017_03.csv',
        'weather_data/523920_2017_03.csv'
    )
