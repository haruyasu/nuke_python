from pymongo import Connection
server = Connection()
db = server["test"]
country_collection = db["country"]

canada = dict()
canada["name"] = "canada"

country_collection.save(canada)
