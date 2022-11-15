"""
Implementation and logic of python workers.
"""
import json
import journalist


class Observer:
    """Class which creates our worker."""

    def __init__(self, url, demand_price, item_name=None):
        """All details that needs our worker in order to observe price properly."""
        self.url = url
        self.demand_price = demand_price
        self.item_name = item_name
        self.work = True

    def save_to_json(self):
        """Function that allows save our workers to json file and then reuse them again."""
        data_to_save = json.dumps({
            "URL": self.url,
            "PRICE": self.demand_price,
            "NAME": self.item_name
        })
        with open(f"{self.item_name}.json", "w", encoding="utf-8") as file:
            file.write(data_to_save)

    def check_price(self):
        """Function that checks if price fullfill our demands."""
        return journalist.get_price(self.url)
