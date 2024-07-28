''' Tools for downloading and combining Premier League season data. '''

import pandas as pd

def download_premier_league_season_data(season: str):
    """
    Downloads the Premier League season data for the specified season.

    Args:
      season (str): The season for which to download the data.

    Returns:
      pandas.DataFrame: The Premier League season data for the specified season.
    """
    return pd.read_csv(f'https://www.football-data.co.uk/mmz4281/{season}/E0.csv')
