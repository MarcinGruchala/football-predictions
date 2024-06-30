'''
Creates combined Premier League data for all seasons in data/raw/premier_league.
Encodes the data and saves it as a CSV in data/interim/premier_league.
'''
import os
import pandas as pd
from tools.convert_date import convert_date
from tools.encoding import encode_team_names
from tools.encoding import encode_result
import premier_league as pl

INPUT_FOLDER = 'data/raw/premier_league'
OUTPUT_DESTINATION_FOLDER = 'data/interim/premier_league'

# Ensure the destination directory exists
if not os.path.exists(OUTPUT_DESTINATION_FOLDER):
    os.makedirs(OUTPUT_DESTINATION_FOLDER)


def prepare_interim_data_frame(df):
    '''
    Encodes the raw data and saves it as a CSV in the interim data folder.
    
    '''
    # Convert the date column to pandas datetime
    df['Date'] = df['Date'].apply(convert_date)

    # Encode team names
    home_encoded, away_encoded, teams_dict = encode_team_names(df['HomeTeam'], df['AwayTeam'],True)
    df['HomeTeamCode'] = home_encoded
    df['AwayTeamCode'] = away_encoded

    # Encode the match results
    df['FTR_code'] = df['FTR'].apply(encode_result)
    df['HTR_code'] = df['HTR'].apply(encode_result)

    return df, teams_dict

print('*** Encoding Premier League data ***')

# Ensure the destination directory exists
if not os.path.exists(OUTPUT_DESTINATION_FOLDER):
    os.makedirs(OUTPUT_DESTINATION_FOLDER)

for season in pl.SEASONS:
    # Read the data for the season
    data = pd.read_csv(f'{INPUT_FOLDER}/premier_league_{season}.csv')

    # Encode the data
    data, encoding_dict = prepare_interim_data_frame(data)

    #Save the team encoding
    with open(f'{OUTPUT_DESTINATION_FOLDER}/team_encoding_{season}.txt', 'w', encoding='utf-8') as file:
        for team, code in encoding_dict.items():
            file.write(f"{team}: {code}\n")

    # Save the data as a CSV
    data.to_csv(f'{OUTPUT_DESTINATION_FOLDER}/premier_league_{season}.csv', index=False)
    print(f'Successfully encoded and saved premier_league_{season}.csv')


premier_league_data = pd.read_csv(f'{INPUT_FOLDER}/premier_league_combined.csv')

# Encode the data
premier_league_data, combined_dict = prepare_interim_data_frame(premier_league_data)

# Save the data as a CSV
premier_league_data.to_csv(f'{OUTPUT_DESTINATION_FOLDER}/premier_league_combined.csv', index=False)
#Save the team encoding
with open(f'{OUTPUT_DESTINATION_FOLDER}/team_encoding_combined.txt', 'w', encoding='utf-8') as file:
    for team, code in combined_dict.items():
        file.write(f"{team}: {code}\n")

print('Successfully encoded and saved premier_league_combined.csv')
print('*** Encoding premier league complete ***')
