"""Module which is used in order to obtain multiple workers from json or csv files"""
import logging
import worker


def create_workers(data, mode):
    """Function that creates worker list and return it as objects in list."""
    observator = worker.Observer
    if mode == "json":
        pass
    elif mode == "csv":
        data_map = map(lambda x: x, data)
        data_list = list(data_map)
        workers = map(lambda x: observator(x[0], x[1], x[2]), data_list)
        return list(workers)
    else:
        return logging.info("This mode doesn't exist.")
