''' Download raw data for Serie A'''

import os
import pandas as pd
from ..configuration import SEASONS
from .tools import download_serie_a_season_data

DESTINATION_FOLDER = 'data/raw/serie_a'

print('*** Downloading Serie A data ***')

# Ensure the destination directory exists
if not os.path.exists(DESTINATION_FOLDER):
    os.makedirs(DESTINATION_FOLDER)

files = []

for season in SEASONS:
    try:
        # Download the season data
        file = download_serie_a_season_data(season)
        # Verify that file is a DataFrame
        if isinstance(file, pd.DataFrame):
            # Save the file as a CSV
            file.to_csv(f'{DESTINATION_FOLDER}/serie_a_{season}.csv', index=False)
            files.append(file)
            print(f'Successfully downloaded and saved serie_a_{season}.csv')
        else:
            print(f'Error: The downloaded data for season {season} is not a DataFrame')
    except Exception as e:
        print(f'Failed to download data for season {season}: {e}')


# Create a combined data frame and save it as a CSV
combined = pd.concat(files)
combined.to_csv(f'{DESTINATION_FOLDER}/serie_a_combined.csv', index=False)

print('Successfully combined Serie A seasons into serie_a_combined.csv')
print('*** Downloading Serie A data complete ***')
