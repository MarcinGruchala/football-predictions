''' Configuration file for data collection and processing. '''

RAW_DATA_PATH = 'data/raw'
INTERIM_DATA_PATH = 'data/interim'
PROCESSED_DATA_PATH = 'data/processed'

LEAGUES = ['premier_league', 'serie_a', 'la_liga']

SEASONS = ['2324', '2223', '2122', '2021', '1920', '1819', '1718', '1617']

ROLLING_AVERAGES_COLUMNS = [
    'FTHG', 'FTAG', 'HTHG', 'HTAG',
    'HS', 'AS', 'HST', 'AST', 'HC', 'AC',
    'HF', 'AF', 'HY', 'AY', 'HR', 'AR', 'FTR_code', 'HTR_code'
]

ROLLING_AVERAGES_WINDOW_SIZES = [2,3,4]
