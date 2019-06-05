import pymongo
from bson.objectid import ObjectId
 
uri = 'mongodb://c4e:12345678Abc@ds231307.mlab.com:31307/c4e'
 
client = pymongo.MongoClient(uri)
db = client.c4e
collection = db.nbhoa

def update_food_by_id(food_id,name,price): 
    collection.update_one({"_id":ObjectId(food_id)},
    {"$set":{"name":name,"price":price}})

def get_food_by_id(food_id): 
    return collection.find_one({"_id":  ObjectId(food_id)})

def get_all(): 
    return list(collection.find())


def insert_food(name, price):
    db.nbhoa.insert_one({"name": name, "price": price})

# def insert_user(name:str ,age:int ):
#     collection = db.nbhoa
#     collection.insert_one({"name":"hoa"})


# import pymongo

# # Kết nối đến database mongodb
# client = pymongo.MongoClient(
#     "mongodb://c4e:12345678Abc@mongodb-2869-0.cloudclusters.net:10011/abc?authSource=admin")

# # tạo db test 1
# db = client.c4e

# # Thêm 1 user vào collection users (collection sẽ tự tạo nếu chưa có)
# db.users.insert_one({'name': 'Hoa', 'age': 30})
# db.users.insert_one({'name': 'Lan', 'age': 25})


#
