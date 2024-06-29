'''
Creates combined Premier League data for all seasons in data/raw/premier_league.
Encodes the data and saves it as a CSV in data/interim/premier_league.
'''
import os
import pandas as pd
from tools.convert_date import convert_date
import premier_league as pl


DESTINATION_FOLDER = 'data/interim/premier_league'

# Ensure the destination directory exists
if not os.path.exists(DESTINATION_FOLDER):
    os.makedirs(DESTINATION_FOLDER)

print('*** Encoding Premier League data ***')

for season in pl.SEASONS:
    # Read the data for the season
    data = pd.read_csv(f'data/raw/premier_league/premier_league_{season}.csv')
    # Convert the date column to pandas datetime
    data['Date'] = data['Date'].apply(convert_date)
    # Save the data as a CSV
    data.to_csv(f'data/interim/premier_league/premier_league_{season}.csv', index=False)
    print(f'Successfully encoded and saved premier_league_{season}.csv')


premier_league_data = pd.read_csv('data/raw/premier_league/premier_league_combined.csv')

# Convert the date column to pandas datetime
premier_league_data['Date'] = premier_league_data['Date'].apply(convert_date)

# Save the data as a CSV
premier_league_data.to_csv('data/interim/premier_league/premier_league_combined.csv', index=False)

print('Successfully encoded and saved premier_league_combined.csv')
print('*** Encoding premier league complete ***')
