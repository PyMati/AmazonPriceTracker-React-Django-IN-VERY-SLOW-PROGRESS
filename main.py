"""Administrator module"""
import worker_creator
import file_reader

data = file_reader.read_csv("None.csv")
wrk = worker_creator.create_workers(file_reader.read_json("D:\ProgramingALL\AmazonPriceTracker\ Phone1.json"), "json")
print(wrk.check_price())
