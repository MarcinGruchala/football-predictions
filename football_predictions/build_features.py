''' This module contains functions for generating features from the data. '''

def generate_rolling_features(rolling, window_sizes):
    """
    Generate feature names for rolling window calculations.

    Args:
        rolling (list): A list of feature names to be used for rolling calculations.
        window_sizes (list): A list of window sizes for the rolling calculations.

    Returns:
        list: A list of strings representing the feature names for each combination
              of rolling feature and window size.
    """
    return [f"rolling_{feature}_w{size}" for feature in rolling for size in window_sizes]

def create_features_from_data_frame(df, rolling_features):
    """
    Create a new DataFrame with selected features from the input DataFrame.

    Args:
        df (pandas.DataFrame): The input DataFrame containing the data.
        rolling_features (list): A list of rolling features to include in the new DataFrame.

    Returns:
        pandas.DataFrame: A new DataFrame with the selected features.

    """
    features = ['HomeTeamCode', 'AwayTeamCode'] + rolling_features
    return df[features]

def create_target_from_df(df, target_column='FTR_code'):
    """
    Create a target variable from a DataFrame.

    Parameters:
        df (pandas.DataFrame): The input DataFrame.
        target_column (str): The name of the target column in the DataFrame. Default is 'FTR_code'.

    Returns:
        pandas.Series: The target variable as a pandas Series.
    """
    return df[target_column]
