import random
import pymongo
SERVER = pymongo.MongoClient()
DB = SERVER['nuke']
USER_COLLECTION = DB['users']

USER_COLLECTION.drop()

users_list = [
"Hugo Leveille",
"Zena Dennett",
"Jarvis Armstong",
"Collin Somma",
"Bobbie Sunderland",
"Orpha Hon",
"Britni Pankratz",
"Ginger Bott",
"Thora Dallman",
"Micaela Toman",
"Georgina Ackman",
"Gus Bowe",
"Kay Hazelrigg",
"Charlesetta Hodes",
"Leanne Burkhardt",
"Laverna Gorby",
"Lisandra Kuhlman",
"Audrea Gerth",
"Breana Forys",
"Sylvia Nicoll",
"Andrew Chiou",
"Loria Kotek",
"Lanita Meagher",
"Damon Sepeda",
"Tula Kapp",
"Lamonica Buhler",
"Elden Repp",
"Pura Mcadory",
"Elidia Cuddy",
"Javier Gunning",
"Vernice Choe",
"Rhona Peppard",
"Alfonso Kuzma",
"Lani Meraz",
"Joline Hazelton",
"Noel Jonason",
"Vi Monfort",
"Neta Henneman",
"Arden Lively",
"Rickie Aman",
"Margert Ridgley",
"Tamatha Tuft",
"Meta Kamin",
"Ferdinand Thormahlen",
"Leif Snoddy",
"Penney Feinstein",
"Claudine Ulm",
"Mckenzie Benware",
"Grazyna Lasky",
"Liz Russel",
"Edgardo Wetherington"]

for name in users_list:
    doc = dict()
    doc['name'] = name
    doc['login'] = name[0].lower() + name.split(" ")[-1].lower()
    doc['email'] = "%s@nuke.com" % name.lower().replace(" ","_")
    doc['age'] = random.randint(18,60)
    USER_COLLECTION.save(doc)
