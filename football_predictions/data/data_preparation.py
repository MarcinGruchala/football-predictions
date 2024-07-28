''' One scrip for preparation data ready to be used based on configuration file ''' 

import os
import pandas as pd
from .configuration import LEAGUES, RAW_DATA_PATH
from .tools.raw import download_raw_data_for_league
from .tools.interim import create_interim_data_for_league, create_interim_data_for_combined_leagues
from .tools.processed import create_processed_data_for_league
from .tools.processed import create_processed_data_for_combined_leagues
from .premier_league.tools import download_premier_league_season_data
from .la_liga.tools import download_la_liga_season_data
from .serie_a.tools import download_serie_a_season_data

# Function to combine all *_combined.csv files in a folder
def combine_csv_files(main_folder):
    ''' Combine all *_combined.csv files in a folder '''

    combined_df_list = []
    for root, _, files in os.walk(main_folder):
        for file in files:
            if file.endswith("_combined.csv"):
                file_path = os.path.join(root, file)
                df = pd.read_csv(file_path)
                combined_df_list.append(df)
    combined_df_inner = pd.concat(combined_df_list, ignore_index=True)
    return combined_df_inner

def main():
    ''' Main function to prepare data for all leagues '''
    # Download raw data for leagues from configuration file
    # Because each league has slightly different download URL I have to do it manually
    download_raw_data_for_league('serie_a',download_serie_a_season_data)
    download_raw_data_for_league('premier_league',download_premier_league_season_data)
    download_raw_data_for_league('la_liga',download_la_liga_season_data)
    raw_combined = combine_csv_files(RAW_DATA_PATH)
    raw_combined.to_csv(f'{RAW_DATA_PATH}/raw_combined.csv', index=False)

    for league in LEAGUES:
        create_interim_data_for_league(league)
    create_interim_data_for_combined_leagues()

    for league in LEAGUES:
        create_processed_data_for_league(league)
    create_processed_data_for_combined_leagues()

    print('*** Data preparation complete ***')

if __name__ == "__main__":
    main()
