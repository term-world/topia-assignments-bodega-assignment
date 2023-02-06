import os
import json

from glob import glob
from rich.table import Table
from rich.console import Console


class Counter:
    def __init__(self):
        self.inventory = self.do_inventory()
        self.bodega_name = os.getcwd().split("/")[-1]
        self.inventory_list = self.tabulate()

    @classmethod
    def do_inventory(self) -> dict:
        items = {}
        for register in glob("./stockroom/*/.registry"):
            category = register.split("/")
            with open(register, "r") as fh:
                items[category[2]] = json.load(fh)
        return items

    def tabulate(self) -> Table:
        table = Table(title=f"{self.bodega_name} Bodega Inventory")

        table.add_column("Department")
        table.add_column("Item")

        for department in self.inventory:
            for item in self.inventory[department]:
                file = os.path.basename(item)
                item = os.path.splitext(file)
                table.add_row(department, item[0])
        return table


def main():
    c = Counter()
    console = Console()
    console.print(c.tabulate())


if __name__ == "__main__":
    main()
