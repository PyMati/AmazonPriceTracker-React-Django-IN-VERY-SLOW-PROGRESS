"""
    Module that allows user to
    provide his data for worker in 2 formats .csv and .json
"""
import json
import logging
import pandas as pd


def read_json(filepath):
    """
    Function that reads json file.
    """
    with open(filepath, "r+", encoding="utf-8") as json_file:
        return json.load(json_file)

def read_csv(filepath):
    """
    Function that reads csv file.
    Structure of the file:
    URL, PRICE, NAME
    """
    try:
        data_file = pd.read_csv(filepath)
        return data_file.to_numpy()
    except pd.errors.EmptyDataError:
        return logging.error("Empty CSV")
