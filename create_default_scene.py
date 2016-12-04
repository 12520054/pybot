#this script to demo create default scene data (game map)
import jsonpickle
from GameModels.SceneConnectionData import SceneConnectionData

from GameModels.SceneData import SceneData

listDefaultScene = list()
default_scene_data_path = 'db/defaultscene/default_scene.json'

listDefaultScene.append(
    SceneData(0,
              'Living room of House',
              'You are standing in an living room of a white house. There is a small mailbox on the table here.',
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
              'Opening the small mailbox reveals a leaflet.. Hmm, you want to read it?',
              -1,
              [],
              [SceneConnectionData(3, ['y', 'yes', 'read leaflet', 'read the leaflet', 'read'])]
              )
)

listDefaultScene.append(
    SceneData(3,
              'Reading...',
              'WELCOME TO PyZORK! \n' +
              'PyZORK is a game of adventure, danger, and cunning.\n' +
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
              [SceneConnectionData(3, ['take the leaflet', 'read the leaflet', 'take leaflet', 'read leaflet']),
               SceneConnectionData(5, ['go out', 'go outsite', 'out the room'])]
              )
)

listDefaultScene.append(
    SceneData(5,
              'Outsite of the house',
              'You are in front of the house.' + '\n' +
              'A path leads into the Forest to the East.',
              -1,
              [],
              [SceneConnectionData(0, ['back', 'insite the house', 'back room']),
               SceneConnectionData(6, ['go e', 'go east', 'east'])]
              )
)

listDefaultScene.append(
    SceneData(
        6,
        'Forest Path',
        'This is a path winding through a dimly lit forest.' + '\n' +
        'One particularly large tree with some low branches stands at the edge of the path.' +
        '\nKeep go East you can see a River, something great waiting for you.',
        -1,
        [],
        [SceneConnectionData(7, ['climp', 'climp tree']),
         SceneConnectionData(5, ['back', 'back to village']),
         SceneConnectionData(9, ['go e', 'go east', 'east'])]
    )
)

listDefaultScene.append(
    SceneData(
        7,
        'Up the Tree',
        'You are about 10 feet above the ground nestled among some large branches.' + '\n' +
        'The nearest branch above you is above your reach.' + '\n' +
        'Beside you on the branch is a small bird\'s nest.' + '\n' +
        'In the bird\'s nest is a large egg encrusted with precious jewels.' + '\n' +
        'WOW! It is exactly a Wood Tresure of NATURE ELEMENTS',
        -1,
        [],
        [SceneConnectionData(6, ['climb down']),
         SceneConnectionData(8, ['take', 'yes', 'take it'])]
    )
)

listDefaultScene.append(
    SceneData(
        8,
        'Taked the Wood Tresure element',
        'The Wood tresure elemnt is now in your inventory!' + '\n' +
        'You must to climb down then find 4 other to win the PyZork!',
        1,
        [],
        [SceneConnectionData(6, ['climb down'])]
    )
)

listDefaultScene.append(
    SceneData(
        9,
        'River Flowing',
        'There is a large river flowing in front of you. Something glisten insite the river with blue light. It is look like very valuable.',
        -1,
        [],
        [SceneConnectionData(11, ['keep going', 'keep walking', 'walk through', 'cross river', 'cross the river']),
         SceneConnectionData(10, ['take blue light', 'take tresure']),
         SceneConnectionData(6, ['back'])]
    )
)

listDefaultScene.append(
    SceneData(
        10,
        'Insite the River',
        'WOW! The Tresure chose you. It is really WATER TRESURE of NATURE ELEMENTS. You got it.' +
        '\nRemember, You have to find 5 Tresures of NATURE ELEMENTS, then bring it to Temple of Nature.',
        3,
        [],
        [SceneConnectionData(9, ['back']),
         SceneConnectionData(11, ['keep going', 'keep walking', 'cross the river', 'cross river'])]
    )
)

listDefaultScene.append(
    SceneData(
        11,
        'Volcano',
        'There is a Hurge Volcano here. It is look very dangerous. On top the Volcano have a Gem with red glisten, shining and very precious.',
        -1,
        [],
        [SceneConnectionData(9, ['back', 'back to river']),
         SceneConnectionData(12, [])]
    )
)

listDefaultScene.append(
    SceneData(
        12,
        'Top of Volcano',
        'Yeah, We all know it is dangerous but you did it completely! You got the Fire Tresure of NATURE ELEMENTS...' +
        '\nTake a look, there no way to keep going. We need go back the village and find orther tresures.',
        4,
        [3],
        [SceneConnectionData(5, ['back the village', 'back'])]
    )
)

list_scene_json = jsonpickle.encode(listDefaultScene)

file = open(default_scene_data_path, 'w')
file.write(list_scene_json)
file.close()

print('Saved Default!')
