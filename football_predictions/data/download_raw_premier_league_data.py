'''Download raw data for Premier League'''
import os
import pandas as pd
import premier_league as pl

DESTINATION_FOLDER = 'data/raw/premier_league'

SEASONS = ['2324', '2223', '2122', '2021', '1920', '1819', '1718', '1617']

# Ensure the destination directory exists
if not os.path.exists(DESTINATION_FOLDER):
    os.makedirs(DESTINATION_FOLDER)

for season in SEASONS:
    try:
        # Download the season data
        file = pl.download_premier_league_season_data(season)
        # Verify that file is a DataFrame
        if isinstance(file, pd.DataFrame):
            # Save the file as a CSV
            file.to_csv(f'{DESTINATION_FOLDER}/premier_league_{season}.csv', index=False)
            print(f'Successfully downloaded and saved premier_league_{season}.csv')
        else:
            print(f'Error: The downloaded data for season {season} is not a DataFrame')
    except Exception as e:
        print(f'Failed to download data for season {season}: {e}')
