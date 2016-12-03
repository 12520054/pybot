import jsonpickle

from GameModels.ItemData import ItemData

default_item_factory_path = 'db/itemfactory/item_factory.json'

listItemFactory = list()

listItemFactory.append(ItemData(0, 'Metal Elemet', 'Metal Elemet Description'))
listItemFactory.append(ItemData(1, 'Wood Element', 'Wood Element Description'))
listItemFactory.append(ItemData(2, 'Earth Element', 'Earth Element Description'))
listItemFactory.append(ItemData(3, 'Water Element', 'Water Element Description'))
listItemFactory.append(ItemData(4, 'Fire Element', 'Fire Element Description'))

list_item_json = jsonpickle.encode(listItemFactory)


file = open(default_item_factory_path, 'w')
file.write(list_item_json)
file.close()

print('Saved Default!')
