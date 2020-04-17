from bson.objectid import ObjectId
from datetime import datetime
from pymongo import MongoClient

from brprev_cli.settings import settings

mongo = MongoClient(settings.MONGO_HOST, settings.MONGO_PORT)
db = mongo['brprev']


def save_search(keywords, result):
    collection = db['searchs']
    result = collection.insert_one(dict(keywords=keywords, created_at=datetime.utcnow(), result=result))
    return result.inserted_id


def get_search(id):
    collection = db['searchs']
    return collection.find_one({'_id': ObjectId(id)})
