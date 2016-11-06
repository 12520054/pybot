#this script to demo create default scene data (game map)
from GameModels.SceneData import SceneData
from GameModels.SceneConnectionData import SceneConnectionData
import jsonpickle
import os


listDefaultScene = list()
default_scene_data_path = 'db/defaultscene/default_scene.json'

listDefaultScene.append(
    SceneData(0, 'Scene 1', 'Description Scene 1', -1, [], [SceneConnectionData(2, ['key word 1', 'key word 2'])])
)

listDefaultScene.append(
    SceneData(1, 'Scene 2', 'Description Scene 2', 1, [], [SceneConnectionData(3, ['key word 1', 'key word 2']), SceneConnectionData(4, ['key word 3', 'key word 4'])])
)

listDefaultScene.append(
    SceneData(2, 'Scene 3', 'Description Scene 3', -1, [], [SceneConnectionData(4, ['key word 1', 'key word 2'])])
)

listDefaultScene.append(
    SceneData(3, 'Scene 4', 'Description Scene 4', 3, [], [])
)

list_scene_json = jsonpickle.encode(listDefaultScene)

file = open(default_scene_data_path, 'w')
file.write(list_scene_json)
file.close()

print('Saved Default!')