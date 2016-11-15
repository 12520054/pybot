# Class Item in Game


class ItemData:
    Id = -1
    Name = ''
    Description = ''

    def __init__(self, itemId, itemName, itemDesc):
        self.Id = itemId
        self.Name = itemName
        self.Description = itemDesc
        pass
