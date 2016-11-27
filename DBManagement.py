#DB Management
#To create new user, query or do everthing with mongodb


from pymongo import MongoClient

db_name = 'text-game-db'
users_collection = 'text-game-db-user'
game_scene_collaction = 'text-game-db-game-scene'


class DBManagement:

    def __init__(self):
        client = MongoClient()
        db = client[db_name]
        users = db[users_collection]
        scenes = db[users_collection]

        pass

    def create_new_user(self, user_id, user_name):

        pass

    def update_user(self, user_id):

        pass

