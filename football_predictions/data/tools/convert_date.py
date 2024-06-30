''' 
This function converts a date string to a datetime object
and then back to a string with the format 'dd/mm/yyyy'. 
'''

import pandas as pd

def convert_date(date_str):
    '''
    Convert a date string to a datetime object and then back to a string
    with the format 'dd/mm/yyyy
    '''
    if len(date_str.split('/')[-1]) == 2:
        return pd.to_datetime(date_str, format='%d/%m/%y').strftime('%d/%m/%Y')

    return pd.to_datetime(date_str, format='%d/%m/%Y').strftime('%d/%m/%Y')
