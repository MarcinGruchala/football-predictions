''' Functions to encode data '''

from sklearn.preprocessing import LabelEncoder
import pandas as pd
pd.options.mode.copy_on_write = True

def convert_date(date_str):
    '''
    Convert a date string to a datetime object and then back to a string
    with the format 'dd/mm/yyyy
    '''
    if len(date_str.split('/')[-1]) == 2:
        return pd.to_datetime(date_str, format='%d/%m/%y').strftime('%d/%m/%Y')

    return pd.to_datetime(date_str, format='%d/%m/%Y').strftime('%d/%m/%Y')

def encode_team_names(home_team, away_team, generate_dictionary=False):
    """
    Encode the given home_team and away_team columns.

    Parameters:
    home_team (pd.Series): The column containing home team names.
    away_team (pd.Series): The column containing away team names.
    generate_dictionary (bool): Flag to indicate whether to generate 
    a dictionary mapping team codes to team names.

    Returns:
    pd.Series, pd.Series, (optional) dict: Two Series objects containing 
    the encoded team names for home_team and away_team,
    and optionally a dictionary mapping team codes to team names.
    """
    # Initialize label encoder
    le = LabelEncoder()

    # Combine home_team and away_team to ensure all unique teams are encoded consistently
    all_teams = pd.concat([home_team, away_team]).unique()
    le.fit(all_teams)

    # Apply label encoding to home_team and away_team
    home_team_code = le.transform(home_team)
    away_team_code = le.transform(away_team)

    if generate_dictionary:
        # Create a dictionary mapping team codes to team names
        team_mapping = {index: label for index, label in enumerate(le.classes_)}
        return pd.Series(home_team_code), pd.Series(away_team_code), team_mapping

    return pd.Series(home_team_code), pd.Series(away_team_code)

def encode_result(result):
    """
    Encodes a match result into a numerical value.

    This function converts the match result from a categorical format ('H', 'D', 'A')
    into a numerical format. The encoding is as follows:
    - 'H' (Home Win) is encoded as 1
    - 'D' (Draw) is encoded as 0
    - 'A' (Away Win) is encoded as -1
    If the input is not one of these values, the function returns None.

    Parameters:
    result (str): The result of the match to be encoded. Expected values are:
                  'H' for Home Win, 'D' for Draw, and 'A' for Away Win.

    Returns:
    int or None: The encoded result as an integer (1, 0, or -1), or None if the input is invalid.

    Examples:
    >>> encode_result('H')
    1
    >>> encode_result('D')
    0
    >>> encode_result('A')
    -1
    >>> encode_result('X')
    None
    """
    if result == 'H':
        return 1
    elif result == 'D':
        return 0
    elif result == 'A':
        return -1
    else:
        return None

def encode_base_data(df):
    """
    Encodes the base data in the given DataFrame.

    Parameters:
    - df: pandas DataFrame
        The DataFrame containing the base data.

    Returns:
    - df: pandas DataFrame
        The DataFrame with the base data encoded.
    """
    # Process date column
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
    # Encode team names
    home_encoded, away_encoded, _ = encode_team_names(df['HomeTeam'], df['AwayTeam'],True)
    df['HomeTeamCode'] = home_encoded
    df['AwayTeamCode'] = away_encoded

    df['FTR_code'] = df['FTR'].apply(encode_result)
    df['HTR_code'] = df['HTR'].apply(encode_result)
    return df
