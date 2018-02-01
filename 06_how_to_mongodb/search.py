# How to use MongoDB Basic api
from pymongo import MongoClient

server = MongoClient()
db = server["test"]
collection = db["users"]

# search = collection.find({"age":20, "country":"canada"})
# print search.count()
# for i in search:
#     print i

# search = collection.find({"age":{"$lte":25}}) #less than xx
# search = collection.find({"age":{"$gte":25}, "country":"usa"}) #greater than xx
# print search.count()
# for i in search:
#     print i

# search = collection.find({"country":"canada"}, {"first_name":1, "_id":0}).limit(10)
# for i in search:
#     print i

# search = collection.find({"$or":[{"age":30}, {"country":"usa"}]})
# for i in search:
#     print i

# search = collection.find({"country":{"$in":["canada", "usa"]}}).sort("first_name", -1)
# for i in search:
#     print i

search = collection.find_one({"first_name":"Liam", "last_name":"Jackson"})
search["age"] = 25
collection.save(search)
print search
