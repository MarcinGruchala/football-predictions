'''Download raw data for Premier League'''
import os
import pandas as pd
import premier_league as pl

DESTINATION_FOLDER = 'data/raw/premier_league'

# Ensure the destination directory exists
if not os.path.exists(DESTINATION_FOLDER):
    os.makedirs(DESTINATION_FOLDER)

print('*** Downloading Premier League data ***')

files = []

for season in pl.SEASONS:
    try:
        # Download the season data
        file = pl.download_premier_league_season_data(season)
        # Verify that file is a DataFrame
        if isinstance(file, pd.DataFrame):
            # Save the file as a CSV
            file.to_csv(f'{DESTINATION_FOLDER}/premier_league_{season}.csv', index=False)
            files.append(file)
            print(f'Successfully downloaded and saved premier_league_{season}.csv')
        else:
            print(f'Error: The downloaded data for season {season} is not a DataFrame')
    except Exception as e:
        print(f'Failed to download data for season {season}: {e}')

# Create a combined data frame and save it as a CSV
combined = pd.concat(files)
combined.to_csv(f'{DESTINATION_FOLDER}/premier_league_combined.csv', index=False)

print('Successfully combined premier league seasons into premier_league_combined.csv')
print('*** Downloading Premier League data complete ***')
