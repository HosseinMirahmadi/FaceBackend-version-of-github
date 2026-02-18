from pymongo.mongo_client import MongoClient

uri = "mongodb://mongo:27017/"

client = MongoClient(uri)
db = client.face_rec_db

ping_collection = db["ping_logger"]
face_collection = db["face"]
