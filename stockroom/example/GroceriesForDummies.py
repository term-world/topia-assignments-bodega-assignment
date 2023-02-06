from inventory.Item import ItemSpec

class GroceriesForDummies(ItemSpec):

  consumable = True

  def __init__(self):
    super().__init__(__file__)
