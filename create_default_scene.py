#this script to demo create default scene data (game map)
import jsonpickle
from GameModels.SceneConnectionData import SceneConnectionData

from GameModels.SceneData import SceneData

listDefaultScene = list()
default_scene_data_path = 'wsgi/db/defaultscene/default_scene.json'

listDefaultScene.append(
    SceneData(0, 'Scene 1', 'Description Scene 1', -1, [],
              [SceneConnectionData(1, ['key word 1', 'key word 2'])])
)

listDefaultScene.append(
    SceneData(1, 'Scene 2', 'Description Scene 2', 1, [1],
              [SceneConnectionData(2, ['key word 1', 'key word 2']), SceneConnectionData(3, ['key word 3', 'key word 4'])])
)

listDefaultScene.append(
    SceneData(2, 'Scene 3', 'Description Scene 3', -1, [],
              [SceneConnectionData(3, ['key word 1', 'key word 2'])])
)

listDefaultScene.append(
    SceneData(3, 'Scene 4', 'Description Scene 4', 3, [],
              [])
)

list_scene_json = jsonpickle.encode(listDefaultScene)

file = open(default_scene_data_path, 'w')
file.write(list_scene_json)
file.close()

print('Saved Default!')
