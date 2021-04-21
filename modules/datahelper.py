import pandas as pd
import config


def load_ais_dataset(url):
    print("Loading data from " + url)
    df = pd.read_csv(url, parse_dates = ['timestamp'])
    df = df.sort_values(by=['timestamp'])
    return df

def load_ais_data_fi_one_week_2018():
    return load_ais_dataset(config.ais_data_fi_one_week_2018_url)

def load_ais_data_fi_10_minutes_2018():
    return load_ais_dataset(config.ais_data_fi_10_minutes_2018_url)
