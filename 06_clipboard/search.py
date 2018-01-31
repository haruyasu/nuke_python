from pymongo import MongoClient

server = MongoClient()
db = server["test"]
collection = db["users"]
search = collection.find({"age":20})

# for i in search:
#     print i["country"]

print search.count()

19:49
