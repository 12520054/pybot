#this script to demo create default scene data (game map)
import jsonpickle
from GameModels.SceneConnectionData import SceneConnectionData
from GameModels.SceneData import SceneData

listDefaultScene = list()
default_scene_data_path = 'db/defaultscene/default_scene.json'

#start scene 1
listDefaultScene.append(
    SceneData(0,
              'In the living room',
              'You are standing in an living room of a house.' +
              ' There is a small mailbox on the table here.',
              -1,
              [],
              [SceneConnectionData(1, ['take mailbox']),SceneConnectionData(6, ['go out', 'go outside'])]
              )
)

listDefaultScene.append(
    SceneData(1,
              'You take the mailbox..',
              'Do you want to Open it?',
              -1,
              [],
              [SceneConnectionData(0, ['no', 'drop mailbox', 'throw mailbox', 'drop the mailbox', 'throw the mailbox']),
                                   SceneConnectionData(2, ['open', 'yes', 'open the mailbox', 'open mailbox']),SceneConnectionData(6, ['go out', 'go outside'])]
              )
)

listDefaultScene.append(
    SceneData(2,
              'Opening the mailbox ...',
              'Opening the small mailbox reveals a leaflet and a key.',
              -1,
              [],
              [SceneConnectionData(3, ['y', 'yes', 'read leaflet', 'read the leaflet', 'read']),
               SceneConnectionData(6, ['go out', 'go outside'])]
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
              [SceneConnectionData(4, ['drop leaflet']),
               SceneConnectionData(6, ['go out', 'go outside'])]
              )
)

listDefaultScene.append(
    SceneData(4,
              'Droped the leaflet',
              'You drop the leaflet and thinking about the adventure....',
              -1,
              [],
              [SceneConnectionData(3, ['take the leaflet', 'read the leaflet', 'take leaflet', 'read leaflet', 'take mailbox', 'read mailbox']),
               SceneConnectionData(5, ['take key','take the key']),
                SceneConnectionData(6, ['go out', 'go outside'])]
              )
)

listDefaultScene.append(
    SceneData(5,
              'You taked the key!',
              'The key can open the door!',
              5,
              [],
              [SceneConnectionData(6, ['go out', 'go outside'])]
              )
)

listDefaultScene.append(
    SceneData(6,
              'Outsite of the house',
              'You are in front of the house. In the village.' + '\n' +
              'A path leads into the Forest to the East.',
              -1,
              [5],
              [SceneConnectionData(0, ['back', 'insite the house', 'back room']),
               SceneConnectionData(7, ['go east', 'east'])]
              )
)
#end scene 1

#start scene 2
listDefaultScene.append(
    SceneData(
        7,
        'Forest Path',
        'This is a path winding through a dimly lit forest.' + '\n' +
        'There is a large tree with some low branches stands at the end of the path.' +
        '\nKeep go East you can see a River, something great waiting for you.',
        -1,
        [],
        [SceneConnectionData(8, ['find the tree', 'find large tree']),
         SceneConnectionData(6, ['back', 'back to village']),
         SceneConnectionData(11, ['go e', 'go east', 'east']),
         [SceneConnectionData(16, ['find the alchemist', 'find alchemist'])]]
    )
)

listDefaultScene.append(
    SceneData(
        8,
        'Behide the Large Tree',
        'A Large tree, It is the tallest Tree in this Forest. Something waiting for you on top of the Tree.',
        -1,
        [],
        [SceneConnectionData(9, ['climb tree', 'climb the tree'])]
    )
)

listDefaultScene.append(
    SceneData(
        9,
        'Up the Tree',
        'You are about 10 feet above the ground nestled among some large branches.' + '\n' +
        'The nearest branch above you is above your reach.' + '\n' +
        'Beside you on the branch is a small bird\'s nest.' + '\n' +
        'In the bird\'s nest is a large egg encrusted with precious jewels.' + '\n' +
        'WOW! It is exactly a Wood Tresure of NATURE ELEMENTS',
        -1,
        [],
        [SceneConnectionData(8, ['climb down']),
         SceneConnectionData(10, ['take', 'yes', 'take it'])]
    )
)

listDefaultScene.append(
    SceneData(
        10,
        'Taked the Wood Tresure element',
        'The Wood Tresure is now in your inventory!' + '\n' +
        'You can climb down then find 4 other to win the PyZork!',
        1,
        [],
        [SceneConnectionData(7, ['climb down'])]
    )
)
#end scene 2

#start scene 3
listDefaultScene.append(
    SceneData(
        11,
        'River Flowing',
        'There is a large river flowing in front of you. Something glisten inside the river with blue light. It is look like very valuable.' +
        'In the Northwest of the river, It is has a Volcano!!!',
        -1,
        [],
        [SceneConnectionData(13, ['keep going', 'keep walking', 'walk through', 'cross river', 'cross the river']),
         SceneConnectionData(12, ['take blue light', 'take tresure', 'take gem']),
         SceneConnectionData(7, ['back'])]
    )
)

listDefaultScene.append(
    SceneData(
        12,
        'Insite the River',
        'WOW! The Tresure chose you. It is really WATER TRESURE of NATURE ELEMENTS. You got it in your inventory.' +
        '\nRemember, You have to find 5 Tresures of NATURE ELEMENTS, then bring it to Temple of Nature.',
        3,
        [1],
        [SceneConnectionData(9, ['back']),
         SceneConnectionData(13, ['keep going', 'keep walking', 'cross the river', 'cross river'])]
    )
)
#end scene 3

#start scene 4
listDefaultScene.append(
    SceneData(
        13,
        'Volcano',
        'There is a Hurge Volcano here. It is look very dangerous. On top the Volcano have a Gem with red light, shining and very precious.',
        -1,
        [1],
        [SceneConnectionData(11, ['back', 'back to river']),
         SceneConnectionData(14, ['climb', 'rush top volcano', 'climb top', 'climb volcano'])]
    )
)

listDefaultScene.append(
    SceneData(
        14,
        'Top of Volcano',
        'You are here. The Tresure of Fire here!!!',
        -1,
        [3],
        [SceneConnectionData(15, ['take gem', 'take tresure'])]
    )
)

listDefaultScene.append(
    SceneData(
        15,
        'Taked the Tresure!',
        'Yeah, We all know it is dangerous but you did it completely! You got the Fire Tresure of NATURE ELEMENTS...' +
        '\nTake a look, there no way to keep going.' +
        ' We need go back the village and find orther tresures.' +
        ' A alchemist is living in the village, You can ask him about the Fire and Metal Element',
        4,
        [3],
        [SceneConnectionData(6, ['back the village', 'back'])]
    )
)
#end scene 4

#start scene 5
listDefaultScene.append(
    SceneData(
        16,
        'The house of Alchemist',
        'The Alchemist can use Power of the Fire ELement to make a Legend Sword.',
        -1,
        [4],
        [SceneConnectionData(7, ['back']),
         SceneConnectionData(17, ['create sword', 'make sword'])]
    )
)

listDefaultScene.append(
    SceneData(
        17,
        'The Legend Sword maked by the Alchemist',
        '',
        -1,
        [4],
        [SceneConnectionData(18, ['take the sword', 'take sword'])]
    )
)
listDefaultScene.append(
    SceneData(
        18,
        'You taked the Sword!',
        'Now, you need to find the Dragon in the North to kill it, the get the Metal Element!',
        6,
        [],
        [SceneConnectionData(7, ['back'])]
    )
)
#end scene 5

#start scene 6
listDefaultScene.append(
    SceneData(
        19,
        'The Dragon House',
        'The Dragon hehe',
        -1,
        [6],
        [
            # scene connect to somewhere
        ]
    )
)
#end scene 6

list_scene_json = jsonpickle.encode(listDefaultScene)
file = open(default_scene_data_path, 'w')
file.write(list_scene_json)
file.close()
print('Saved Default!')