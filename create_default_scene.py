#this script to demo create default scene data (game map)
import jsonpickle
from GameModels.SceneConnectionData import SceneConnectionData

from GameModels.SceneData import SceneData

listDefaultScene = list()
default_scene_data_path = 'db/defaultscene/default_scene.json'

listDefaultScene.append(
    SceneData(0,
              'West of Village',
              'You are standing in an open field west of a white house, with a boarded front door. There is a small mailbox here.',
              -1,
              [],
              [SceneConnectionData(1, ['open mailbox', 'open the mailbox'])])
)

listDefaultScene.append(
    SceneData(1,
              'Opening the mailbox ...',
              'Opening the small mailbox reveals a leaflet',
              -1,
              [],
              [SceneConnectionData(2, ['read leaflet', 'read the leaflet', 'read'])])
)

listDefaultScene.append(
    SceneData(2,
              'Reading...',
              'WELCOME TO ZORK! \n' +
              'ZORK is a game of adventure, danger, and low cunning.\n' +
              'In it you will explore some of the most amazing territory ever seen by mortals to find 5 TREASURE of NATRURE ELEMENTS.\n' +
              'Let the adventure begin....!',
              -1,
              [],
              [SceneConnectionData(3, ['drop leaflet'])])
)

listDefaultScene.append(
    SceneData(3,
              'Droped the leaflet',
              'You drop the leaflet and thinking about the adventure....',
              -1,
              [],
              [])
)

list_scene_json = jsonpickle.encode(listDefaultScene)

file = open(default_scene_data_path, 'w')
file.write(list_scene_json)
file.close()

print('Saved Default!')
