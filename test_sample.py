"Testing functionality of workers."
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import pytest
import file_reader
import journalist
import worker
import worker_creator


def create_worker():
    try:
        return worker.Observer("URL", "PRICE", "ITEM")
    except:
        return None

def test_create_worker():
    assert create_worker is not None
    