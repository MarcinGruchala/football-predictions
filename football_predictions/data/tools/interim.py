''' Tools for creating interim data. '''

import os
import pandas as pd
from .encoding import encode_team_names, encode_result, convert_date
from ..configuration import SEASONS, COLUMNS_TO_KEEP

def create_interim_data_for_league(league):
    '''
    Encodes the raw data and saves it as a CSV in the interim data folder.
    '''
    print(f'*** Creating interim data for {league} ***')
    input_folder = f'data/raw/{league}'
    output_folder = f'data/interim/{league}'

    # Ensure the destination directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for season in SEASONS:
        # Read the data for the season
        data = pd.read_csv(f'{input_folder}/{league}_{season}.csv')

        # Encode the data
        data, encoding_dict = prepare_interim_data_frame(data)
        useful_data = data[COLUMNS_TO_KEEP]

        # Save the team encoding
        with open(f'{output_folder}/team_encoding_{season}.txt', 'w', encoding='utf-8') as file:
            for team, code in encoding_dict.items():
                file.write(f"{team}: {code}\n")

        # Save the data as a CSV
        useful_data.to_csv(f'{output_folder}/{league}_{season}.csv', index=False)
        print(f'Successfully encoded and saved {league}_{season}.csv')

    raw_combined_data = pd.read_csv(f'{input_folder}/{league}_combined.csv')

    # Encode the data
    combined_data, encoding_dict = prepare_interim_data_frame(raw_combined_data)
    useful_combined_data = combined_data[COLUMNS_TO_KEEP]

    # Save the team encoding
    with open(f'{output_folder}/team_encoding_combined.txt', 'w', encoding='utf-8') as file:
        for team, code in encoding_dict.items():
            file.write(f"{team}: {code}\n")
    # Save the data as a CSV
    useful_combined_data.to_csv(f'{output_folder}/{league}_combined.csv', index=False)
    print(f'Successfully encoded and saved {league}_combined.csv')
    print(f'*** Completed creating interim data for {league} ***')

def create_interim_data_for_combined_leagues():
    ''' Encodes the raw data and saves it as a CSV in the interim data folder. '''
    print('*** Creating interim data for combined leagues ***')
    input_folder = 'data/raw'
    output_folder = 'data/interim'
    data = pd.read_csv(f'{input_folder}/raw_combined.csv')
    # Encode the data
    data, encoding_dict = prepare_interim_data_frame(data)
    useful_data = data[COLUMNS_TO_KEEP]

    # Save the team encoding
    with open(f'{output_folder}/team_encoding_interim_combined.txt', 'w', encoding='utf-8') as file:
        for team, code in encoding_dict.items():
            file.write(f"{team}: {code}\n")
    # Save the data as a CSV
    useful_data.to_csv(f'{output_folder}/interim_combined.csv', index=True)
    print('*** Completed creating interim data for combined leagues ***')

def prepare_interim_data_frame(df):
    '''
    Encodes the raw data and saves it as a CSV in the interim data folder.
    '''
    # Convert the date column to pandas datetime
    df['Date'] = df['Date'].apply(convert_date)

    # Encode team names
    home_encoded, away_encoded, teams_dict = encode_team_names(df['HomeTeam'], df['AwayTeam'], True)

    # Encode the match results
    ftr_encoded = df['FTR'].apply(encode_result)
    htr_encoded = df['HTR'].apply(encode_result)

    # Create a new DataFrame with the new columns
    new_columns = pd.DataFrame({
        'HomeTeamCode': home_encoded,
        'AwayTeamCode': away_encoded,
        'FTR_code': ftr_encoded,
        'HTR_code': htr_encoded
    })

    # Concatenate the original DataFrame with the new columns
    df = pd.concat([df, new_columns], axis=1)

    return df, teams_dict
