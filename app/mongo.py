import pymongo

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client.my_test_db


def get_user_id_from_username(username):
    user = db.users.find_one({"username": username})
    user_id = user["_id"]
    return user_id
