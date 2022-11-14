"Testing functionality of workers."
import pytest
import worker, worker_creator, file_reader, journalist

def create_worker():
    worker.Observer("URL", "PRICE", "ITEM")

def test_create_worker():
    assert create_worker != None