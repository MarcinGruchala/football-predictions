import pandas as pd

def download_premier_league_base_data():
  premier_league_2324 = download_premier_league_season_data('2324')
  premier_league_2223 = download_premier_league_season_data('2223')
  premier_league_2122 = download_premier_league_season_data('2122')
  premier_league_2021 = download_premier_league_season_data('2021')
  premier_league_1920 = download_premier_league_season_data('1920')
  
  # Combine the dataframes into one
  combined = pd.concat([
      premier_league_1920,
      premier_league_2021,
      premier_league_2122,
      premier_league_2223,
      premier_league_2324
      ])
  # Reset the index to avoid any potential issues
  combined.reset_index(drop=True, inplace=True)

  return combined  

def download_premier_league_season_data(season: str):
  return pd.read_csv(f'https://www.football-data.co.uk/mmz4281/{season}/E0.csv')
