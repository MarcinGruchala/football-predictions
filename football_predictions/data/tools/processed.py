''' Tools for creating processed data. '''

import os
import pandas as pd
from ..configuration import ROLLING_AVERAGES_COLUMNS, ROLLING_AVERAGES_WINDOW_SIZES, SEASONS
from .rolling_averages import rolling_averages_for_window_sizes


def create_processed_data_for_league(league):
    '''
    Created processed data for given league.
    '''
    print(f'*** Creating processed data for {league} ***')
    input_folder = f'data/interim/{league}'
    output_folder = f'data/processed/{league}'

    # Ensure the destination directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for season in SEASONS:
        # Read the data for the season
        data = pd.read_csv(f'{input_folder}/{league}_{season}.csv')
        data['Date'] = pd.to_datetime(data['Date'], dayfirst = True)
        data = calculate_rolling_averages_home_team(data)
        data = calculate_rolling_averages_away_team(data)
        data = data.sort_values('Date')

        # Save the data as a CSV
        data.to_csv(f'{output_folder}/{league}_{season}.csv', index=False)
        print(f'Successfully processed and saved {league}_{season}.csv')
    interim_combined_data = pd.read_csv(f'{input_folder}/{league}_combined.csv')
    interim_combined_data['Date'] = pd.to_datetime(interim_combined_data['Date'], dayfirst = True)
    interim_combined_data = calculate_rolling_averages_home_team(interim_combined_data)
    interim_combined_data = calculate_rolling_averages_away_team(interim_combined_data)
    interim_combined_data = interim_combined_data.sort_values('Date')
    interim_combined_data.to_csv(f'{output_folder}/{league}_combined.csv', index=False)
    print(f'Successfully processed and saved {league}_combined.csv')
    print(f'*** Completed creating processed data for {league} ***')



def calculate_rolling_averages_home_team(data_frame):
    """
    Calculate rolling averages for specified columns over specified window sizes for each home team, 
    then return the data sorted by date.

    Parameters:
    data_frame (pd.DataFrame): DataFrame containing match data with at least the following columns:
        - 'HomeTeam': Name of the home team
        - 'Date': Date of the match
        - Columns specified in ROLLING_AVERAGES_COLUMNS

    Returns:
    pd.DataFrame: DataFrame with rolling averages added, reset index, and sorted by date.
    """
    grouped = data_frame.groupby("HomeTeam").apply(
    lambda x:
        rolling_averages_for_window_sizes(
            x,
            ROLLING_AVERAGES_COLUMNS,
            ROLLING_AVERAGES_WINDOW_SIZES,
            'H'
            )
        )
    result = grouped.reset_index(drop=True).sort_values(by="Date")
    return result

def calculate_rolling_averages_away_team(data_frame):
    """
    Calculate rolling averages for specified columns over specified window sizes for each away team, 
    then return the data sorted by date.

    Parameters:
    data_frame (pd.DataFrame): DataFrame containing match data with at least the following columns:
        - 'AwayTeam': Name of the home team
        - 'Date': Date of the match
        - Columns specified in ROLLING_AVERAGES_COLUMNS

    Returns:
    pd.DataFrame: DataFrame with rolling averages added, reset index, and sorted by date.
    """
    grouped = data_frame.groupby("AwayTeam").apply(
    lambda x:
        rolling_averages_for_window_sizes(
            x,
            ROLLING_AVERAGES_COLUMNS,
            ROLLING_AVERAGES_WINDOW_SIZES,
            'A'
            )
        )
    result = grouped.reset_index(drop=True)
    return result
