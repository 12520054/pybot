#this script to demo create default scene data (game map)
import jsonpickle
from GameModels.SceneConnectionData import SceneConnectionData

from GameModels.SceneData import SceneData

listDefaultScene = list()
default_scene_data_path = 'db/defaultscene/default_scene.json'

listDefaultScene.append(
    SceneData(0,
              'Living room of House',
              'You are standing in an living room of a white house, with a boarded front door. There is a small mailbox on the table here.',
              -1,
              [],
              [SceneConnectionData(1, ['take mailbox'])]
              )
)

listDefaultScene.append(
    SceneData(1,
              'You take the mailbox..',
              'Do you want to Open it?',
              -1,
              [],
              [SceneConnectionData(0, ['no', 'drop mailbox', 'throw mailbox', 'drop the mailbox', 'throw the mailbox']),
                                   SceneConnectionData(2, ['open', 'yes', 'open the mailbox', 'open mailbox'])]
              )
)

listDefaultScene.append(
    SceneData(2,
              'Opening the mailbox ...',
              'Opening the small mailbox reveals a leaflet',
              -1,
              [],
              [SceneConnectionData(2, ['read leaflet', 'read the leaflet', 'read'])]
              )
)

listDefaultScene.append(
    SceneData(3,
              'Reading...',
              'WELCOME TO PyZORK! \n' +
              'PyZORK is a game of adventure, danger, and low cunning.\n' +
              'In it you will explore some of the most amazing territory ever seen by mortals to find 5 TREASURES of NATRURE ELEMENTS.\n' +
              'Let the adventure begin....!',
              -1,
              [],
              [SceneConnectionData(4, ['drop leaflet'])]
              )
)

listDefaultScene.append(
    SceneData(4,
              'Droped the leaflet',
              'You drop the leaflet and thinking about the adventure....',
              -1,
              [],
              [SceneConnectionData(3, ['take the leaflet', 'read the leaflet', 'take leaflet', 'read leaflet'])]
              )
)


list_scene_json = jsonpickle.encode(listDefaultScene)

file = open(default_scene_data_path, 'w')
file.write(list_scene_json)
file.close()

print('Saved Default!')
