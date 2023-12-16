import pymongo

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client.my_test_db
