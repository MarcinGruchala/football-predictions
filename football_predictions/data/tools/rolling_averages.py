""" Functions to calculate rolling averages for specified columns in a DataFrame. """ 

import pandas as pd

def rolling_averages(group, cols, new_cols, window_size):
    """
    Calculate rolling averages for specified columns in a DataFrame.

    Parameters:
    group (pd.DataFrame): DataFrame containing the data to be processed.
    cols (list): List of column names to calculate rolling averages for.
    new_cols (list): List of new column names to store the rolling averages.
    window_size (int): Number of consecutive data points to include in the rolling window.

    Returns:
    pd.DataFrame: DataFrame with rolling averages appended as new columns,
    with rows containing NaN values in these new columns removed.
    """
    group = group.sort_values("Date")
    rolling_stats = group[cols].rolling(window=window_size, closed='left').mean()
    group[new_cols] = rolling_stats
    return group


def rolling_averages_for_window_sizes(group, cols, sizes,team):
    """
    Calculate multiple rolling averages for specified columns in a DataFrame,
    for specified window sizes.

    Parameters:
    group (pd.DataFrame): DataFrame containing the data to be processed.
    cols (list): List of column names to calculate rolling averages for.
    window_sizes (list): List of numbers of consecutive data points to 
    include in the rolling window.
    team (string): Label for home or away team

    Returns:
    pd.DataFrame: DataFrame with rolling averages appended as new columns,
    with rows containing NaN values in these new columns removed.
    """
    for window_size in sizes:
        new_rolling_columns = [f'{team}_R_{col}_W_{window_size}' for col in cols]
        rolling_df = rolling_averages(group, cols, new_rolling_columns,
                                    window_size)
        group = group.merge(rolling_df[new_rolling_columns],
                          left_index=True, right_index=True, how='left')
    group = group.dropna(subset=new_rolling_columns)
    return group
