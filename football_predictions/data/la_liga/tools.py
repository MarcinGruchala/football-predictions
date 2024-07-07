''' This module contains tools for downloading La Liga data. '''

import pandas as pd


def download_la_liga_season_data(season):
    """
    Downloads the La Liga season data for the specified season.

    Args:
      season (str): The season for which to download the data.

    Returns:
      pandas.DataFrame: The data for the specified season.
    """
    return pd.read_csv(f'https://www.football-data.co.uk/mmz4281/{season}/SP1.csv')
