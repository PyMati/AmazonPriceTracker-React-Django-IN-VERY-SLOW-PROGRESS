"""Module that allows user to provide his data for worker in 2 formats .csv and .json"""
import json


def read_json(filepath):
    """Function that reads json file."""
    with open(filepath, "r+", encoding="utf-8") as json_file:
        return json.load(json_file)
