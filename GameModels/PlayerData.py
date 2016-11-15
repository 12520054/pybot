#Class Player

#@
# List member var in Playe
# PlayerId: Id of this player - int
# PlayerName: Name of this player - string
# CurrentSceneID: Current Player Position in Game - id
# ListItem: current inventory - ItemData[]
# # # # # #


class PlayerData:

    Id = -1
    Name = ''
    CurrentSceneId = -1
    ListItem = []
    ListScene = []

    def __init__(self, playerId, playerName, currentSceneId, listItem, listScene):
        self.Id = playerId
        self.Name = playerName
        self.CurrentSceneId = currentSceneId
        self.ListItem = listItem
        self.ListScene = listScene
        pass
