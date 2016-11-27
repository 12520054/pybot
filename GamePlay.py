# My Game Here
import os
import json
import jsonpickle
from GameModels.PlayerData import PlayerData
from chatterbot import ChatBot

rootPath = 'db/users/'
default_scene_data_path = 'db/defaultscene/default_scene.json'
item_data_path = 'db/itemfactory/item_factory.json'
alert_create_new_user = 'Undefined command! Use \'CREATE <Space> [Name]\' to create new player.\nHave a good time!'

# basic game cmd
get_status = '@status'
get_list_cmd = '@cmd'
how_to_play_game = '@howto'
reset_game = '@hardreset'


# end basic game cmd


class GamePlay:
    chatbot = ChatBot(
        'Fake Bot',
        trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
    )

    def __init__(self):
        self.chatbot.train("chatterbot.corpus.english")
        pass

    def processUserMessage(self, userId, userMsg):

        file_path = rootPath + userId + '.json'
        if os.path.isfile(file_path):
            user_msg_splited = userMsg.split(' ')

            if reset_game in user_msg_splited:
                os.remove(rootPath + userId + '.json')
                return 'game data reset!\nUse \'CREATE <Space> [Name]\' to create new player.\nHave a good time!'

            # handle get user info
            if get_status in user_msg_splited:
                return 'get user status: bla bla bla....'
            # end handle get user info

            # handle return list cmd (how to play game)
            if get_list_cmd in user_msg_splited:
                return 'get list cmd in game: bla bla bla ....'
            # end handle return list cmd (how to play game)

            # handle how to play game
            if how_to_play_game in user_msg_splited:
                return 'how to play this game.. bla bla bla .....'
            # end handle how to play game

            return self.on_user_turn(userMsg.lower(), file_path)
        else:
            return self.create_user(userId, userMsg.split(' '))
        pass

    def create_user(self, userId, words):

        words_len = len(words)
        if words_len == 2:
            create_cmd = words[0].lower()
            if create_cmd == 'create':
                return self.create_user_data_file(userId, words[1])
            else:
                return alert_create_new_user
        else:
            return alert_create_new_user

        pass

    def create_user_data_file(self, userId, user_name):
        # How to storage User DB?
        player_data = PlayerData(userId, user_name, 0, [], self.get_default_scene_data())
        player_json = jsonpickle.encode(player_data)

        file_name = userId + '.json'
        file_path = rootPath + file_name

        file = open(file_path, 'w')
        file.write(player_json)
        file.close()
        return 'Success to creat new user:  ' + player_data.Name + '.\nUse command @status to view current your status in game.\n @cmd, @howto to learn how to play game :D'
        pass

    def get_default_scene_data(self):
        scene_data = open(default_scene_data_path, 'r')
        result = jsonpickle.decode(scene_data.read())
        scene_data.close()
        return result
        pass

    def on_user_turn(self, user_input, path):

        player_file = open(path, 'r')
        player_json = player_file.read()
        player_file.close()
        player_object = jsonpickle.decode(player_json)

        player_name = player_object.Name
        curr_sceneid = player_object.CurrentSceneId
        list_items = player_object.ListItem
        list_scene = player_object.ListScene

        player_current_scene = player_object.ListScene[curr_sceneid]
        list_connection_scene = player_current_scene.ListConnection

        # handle user scene
        for connection_scene in list_connection_scene:
            if user_input in connection_scene.ListKeyWord:

                scene_data_connected = player_object.ListScene[connection_scene.SceneId]
                if scene_data_connected.check_listitem_require(list_items) is True:

                    save_file = open(path, 'w')
                    player_object.CurrentSceneId = connection_scene.SceneId
                    curr_sceneid = player_object.CurrentSceneId
                    scene_item_id = scene_data_connected.ItemInScene

                    if scene_item_id is not -1:
                        player_object.ListItem.append(scene_item_id)
                        scene_data_connected.ItemInScene = -1
                        player_object.ListScene[connection_scene.SceneId] = scene_data_connected

                    player_json = jsonpickle.encode(player_object)
                    save_file.write(player_json)
                    save_file.close()

                    return 'Next scene: ' + player_object.ListScene[curr_sceneid].SceneName + '\n' + \
                           player_object.ListScene[curr_sceneid].Description

                else:
                    req_items = ''
                    item_file = open(item_data_path, 'r')
                    item_json = item_file.read()
                    item_file.close()
                    list_item_object = jsonpickle.decode(item_json)
                    for itemid in scene_data_connected.ListRequireItems:
                        req_items += (
                        list_item_object[itemid].Name + ': ' + list_item_object[itemid].Description + '\n')
                    return 'You need to find list item: ' + req_items + 'To go next scene!'
        # end handle user scene

        # user wrong input
        return str(self.chatbot.get_response(user_input)) + '\n' + \
               'You current here. The scene info below.\n' + \
               'You\'re at ' + player_object.ListScene[curr_sceneid].SceneName + '\n' + \
               player_object.ListScene[curr_sceneid].Description

        # end user wrong input
        pass
