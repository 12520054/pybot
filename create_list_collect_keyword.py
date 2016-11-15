import jsonpickle

default_data_path = 'wsgi/db/defaultscene/collect_keywords.json'

collect_keywords = ['collect', 'grab']

json = jsonpickle.encode(collect_keywords)

file = open(default_data_path, 'w')
file.write(json)
file.close()

print('Saved Default!')
