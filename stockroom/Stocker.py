import os
import sys
import json
import narrator

from glob import glob
from inventory.Item import Factory

class Stocker:

  @staticmethod
  def stock(folder: str):
    file = f"{folder}.list"
    with open(file, "r") as fh:
      items = fh.readlines()
    os.makedirs(
      folder,
      exist_ok=True
    )
    for item in items:
      item = item.title()
      print(item)
      item = item.replace("-","")
      Factory(item.strip(),folder)

  @staticmethod
  def inventory(folder: str):
    registry = {}
    items = glob(f"{folder}/*.py")
    registry = items
    path = os.path.join(
      folder,
      ".registry"
    )
    with open(path, "w") as fh:
      json.dump(registry, fh, indent = 2)

def main():

  n = narrator.Narrator()

  n.narrate()
  n.path.change({"act": 1, "scene": 0})

  dept = input("Department to stock: ")
  try:
    Stocker.stock(dept)
  except:
    n.path.change({"act": 2, "scene":0})

  n.narrate()

  if n.path.act == 2:
    sys.exit()

  Stocker.inventory(dept)


if __name__ == "__main__":
  main()
