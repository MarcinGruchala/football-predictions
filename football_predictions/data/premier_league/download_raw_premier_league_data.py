'''Download raw data for Premier League'''
from ..tools.raw import download_raw_data_for_league
from .tools import download_premier_league_season_data

download_raw_data_for_league('premier_league',download_premier_league_season_data)
