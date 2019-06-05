uri = 'mongodb://c4e:12345678Abc@ds231307.mlab.com:31307/c4e'
import pymongo
client = pymongo.MongoClient(uri)
db = client.c4e
# collection = db.ltluc
# collection.insert_one({'name':'luc'})
# print(list(db.users.find({})))
# collection.insert_one({'name':'lan','age':40})
# collection.update_one({'name':'lan'},{'$set':{'age':29}})

def insert_one(name:str,age:int):
    """them user
    
    Arguments:
        name {[type]} -- them ten 1 nguoi
        age {[type]} -- them tuoi nguoi can the,
    """
    collection = db.ltluc
    collection.update_one({'name':name},{'$set':{'age':age}})
    # collection.update_one({'name':name},{'$set':{'age':age}})