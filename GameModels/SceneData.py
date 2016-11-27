#Declare SceneDa
# Id type int
# Name type string
# Description type string
# ListLinkedScene type LinkedScene[]ta
# ListItemInScene: Item have in Scene []


class SceneData:

    Id = -1
    SceneName = ''
    Description = ''
    ItemInScene = -1
    ListRequireItems = []  # need type int
    ListConnection = []

    def __init__(self,
                 sceneId,
                 sceneName,
                 sceneDescription,
                 itemInScene,
                 listRequireItems,
                 listSceneConnection):

        self.Id = sceneId
        self.SceneName = sceneName
        self.Description = sceneDescription
        self.ItemInScene = itemInScene
        self.ListRequireItems = listRequireItems
        self.ListConnection = listSceneConnection

        pass

    def check_listitem_require(self, listUserItem):
        print('Start Track List Item')
        print(self.Id)
        print(self.ListRequireItems)
        print('End Track List Item')

        if len(self.ListRequireItems) is 0:
            return True

        if len(listUserItem) is 0:
            return False

        for item in self.ListRequireItems:

            if (item in listUserItem) is False:
                return False

        return True
        pass
