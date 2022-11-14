"""
Implementation and logic of python workers.
"""
import json
import journalist


class Observer:
    """Class which creates our worker."""

    def __init__(self, url, demand_price, item_name="None"):
        """All details that needs our worker in order to observe price properly."""
        self.url = url
        self.demand_price = demand_price
        self.item_name = item_name

    def save_to_json(self):
        """Function that allows save our workers to json file and then reuse them again."""
        data_to_save = json.loads({
            "Url": self.url,
            "Demand price": self.demand_price,
            "Item name": self.item_name
        })
        with open(f"{self.item_name}.json", "w", encoding="utf-8") as file:
            file.write(data_to_save)

    def check_price(self):
        """Function that checks if price fullfill our demands."""
        journalist.get_price(self.url)


URL = "https://www.amazon.pl/Xiaomi-Redmi-9C-NFC-Aurora/dp/B0B2K87MXS/ref=sr_1_1?pd_rd_r=dd9b2b75-a9c4-444e-be0a-945df0ef8c5f&pd_rd_w=uHPeh&pd_rd_wg=hSNaD&pf_rd_p=9d8442c3-20f2-40fc-bc73-6a075a9816ce&pf_rd_r=XHMC4XSPCY7ZF9EX4YEA&qid=1668446430&refinements=p_89%3AXiaomi&rnid=21074364031&s=electronics&sr=1-1"
scrap = Observer(URL, 300)
scrap.check_price()
