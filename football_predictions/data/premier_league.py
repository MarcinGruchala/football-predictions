''' Downloading Premier League Data from Football-Data.co.uk'''

import pandas as pd

SEASONS = ['2324', '2223', '2122', '2021', '1920', '1819', '1718', '1617']

def download_premier_league_base_data():
    """
    Downloads and combines Premier League season data from multiple seasons.

    Returns:
      combined (pandas.DataFrame): Combined data frame containing Premier League season data.
    """
    premier_league_2324 = download_premier_league_season_data('2324')
    premier_league_2223 = download_premier_league_season_data('2223')
    premier_league_2122 = download_premier_league_season_data('2122')
    premier_league_2021 = download_premier_league_season_data('2021')
    premier_league_1920 = download_premier_league_season_data('1920')
    premier_league_1819 = download_premier_league_season_data('1819')
    premier_league_1718 = download_premier_league_season_data('1718')
    # Combine the data frames into one
    combined = pd.concat([
      premier_league_1920,
      premier_league_2021,
      premier_league_2122,
      premier_league_2223,
      premier_league_2324,
      premier_league_1819,
      premier_league_1718
      ])
    # Reset the index to avoid any potential issues
    combined.reset_index(drop=True, inplace=True)

    return combined

def download_premier_league_season_data(season: str):
    """
    Downloads the Premier League season data for the specified season.

    Args:
      season (str): The season for which to download the data.

    Returns:
      pandas.DataFrame: The Premier League season data for the specified season.
    """
    return pd.read_csv(f'https://www.football-data.co.uk/mmz4281/{season}/E0.csv')
