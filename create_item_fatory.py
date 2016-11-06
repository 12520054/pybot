import jsonpickle

from GameModels.ItemData import ItemData

default_item_factory_path = 'wsgi/db/itemfactory/item_factory.json'

listItemFactory = list()

listItemFactory.append(ItemData(1, 'Item 1', 'Item 1 Description'))
listItemFactory.append(ItemData(2, 'Item 2', 'Item 2 Description'))
listItemFactory.append(ItemData(3, 'Item 3', 'Item 3 Description'))
listItemFactory.append(ItemData(4, 'Item 4', 'Item 4 Description'))
listItemFactory.append(ItemData(5, 'Item 5', 'Item 5 Description'))
listItemFactory.append(ItemData(6, 'Item 6', 'Item 5 Description'))

list_item_json = jsonpickle.encode(listItemFactory)


file = open(default_item_factory_path, 'w')
file.write(list_item_json)
file.close()

print('Saved Default!')