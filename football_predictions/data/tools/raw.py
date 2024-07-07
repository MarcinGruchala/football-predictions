''' Tools for creating raw data. '''

import os
import pandas as pd
from ..configuration import SEASONS

def download_raw_data_for_league(league, download_function):
    ''' Downloads raw data for a league. '''
    print(f'*** Downloading {league} data ***')

    destination_folder = f'data/raw/{league}'

    # Ensure the destination directory exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    files = []
    for season in SEASONS:
        file = download_function(season)
        file.to_csv(f'{destination_folder}/{league}_{season}.csv', index=False)
        files.append(file)
        print(f'Successfully downloaded and saved {league}_{season}.csv')
    # Create a combined data frame and save it as a CSV
    combined = pd.concat(files)
    combined.to_csv(f'{destination_folder}/{league}_combined.csv', index=False)
    print(f'Successfully combined {league} seasons into {league}_combined.csv')
    print(f'*** Downloading {league} data complete ***')
