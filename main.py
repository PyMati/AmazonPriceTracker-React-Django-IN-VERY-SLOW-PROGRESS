"""Administrator module"""
import workercreator
import reader

data = reader.read_csv("None.csv")
wrk_list = workercreator.create_workers(data, "csv")
for worker in wrk_list:
    worker.check_price()