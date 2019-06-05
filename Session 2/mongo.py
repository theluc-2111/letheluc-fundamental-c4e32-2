
uri = 'mongodb://c4e:12345678Abc@ds231307.mlab.com:31307/c4e'
import pymongo
client = pymongo.MongoClient(uri)
db = client.c4e

def get_all():
    collection = db.ltluc
    return list(collection.find())

def insert_food(name,price):
    db.ltluc.insert_one({'name':name,'price':price})


