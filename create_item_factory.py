import jsonpickle

from GameModels.ItemData import ItemData

default_item_factory_path = 'db/itemfactory/item_factory.json'
listItemFactory = list()
listItemFactory.append(ItemData(0, 'Metal Elemet', 'Metal Elemet Description'))
listItemFactory.append(ItemData(1, 'Wood Element', 'Wood Element Description'))
listItemFactory.append(ItemData(2, 'Earth Element', 'Earth Element Description'))
listItemFactory.append(ItemData(3, 'Water Element', 'Water Element Description'))
listItemFactory.append(ItemData(4, 'Fire Element', 'Fire Element Description'))
listItemFactory.append(ItemData(5, 'The Key', 'The Key can open the door and go out!'))
listItemFactory.append(ItemData(6, 'The SWord', 'With this Sword, you can kill the Dragon'))
list_item_json = jsonpickle.encode(listItemFactory)
file = open(default_item_factory_path, 'w')
file.write(list_item_json)
file.close()
print('Saved Default!')


