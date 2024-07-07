''' Download raw data for Serie A'''
from ..tools.raw import download_raw_data_for_league
from .tools import download_serie_a_season_data

download_raw_data_for_league('serie_a',download_serie_a_season_data)
