from pymongo import MongoClient
import datetime

server = MongoClient()
db = server["test"]
country_collection = db["country"]
country_collection.drop()

canada = dict()
canada["name"] = "canada"
canada["population"] = 553600055550
canada["foundation"] = datetime.datetime(1874, 04, 03)

usa = dict()
usa["name"] = "usa"
usa["population"] = 4446666
usa["foundation"] = datetime.datetime(2013, 03, 22)

country_collection.insert([canada, usa])
