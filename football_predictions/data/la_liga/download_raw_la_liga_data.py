''' Download raw La Liga data from football-data.co.uk '''

from ..tools.raw import download_raw_data_for_league
from .tools import download_la_liga_season_data

download_raw_data_for_league('la_liga',download_la_liga_season_data)
