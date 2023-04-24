import random
from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime


user = 'pes1ug21cs826'           # username as set for the mongodb admin server (the username used in secret.yaml - before base64 conversion)
password = 'bunker@01'       # password as set for the mongodb admin server (the password used in secret.yaml - before base64 conversion)
host = 'mongodb-service'    # service name of the mongodb admin server as set in mongo-service.yaml
port = 27017              # port number of the mongodb admin server as set in mongo-deployment.yaml
conn_string = f'mongodb+srv://pes1ug21cs826:<bunker@01>@cluster0.0cnxip6.mongodb.net/?retryWrites=true&w=majority'

db = MongoClient(conn_string).blog


nouns = ("puppy", "car", "person")
verbs = ("runs", "jumps", "drives") 
adv = ("crazily.", "dutifully.", "occasionally.")
adj = ("adorable", "clueless", "odd")

for i in range(10):
    createdAt = datetime.now()
    num = random.randrange(0,3)
    title = nouns[num] + ' ' + verbs[num] + ' ' + adj[num] + ' ' + adv[num]
    author = "author " + str(i)
    db.posts.insert_one({"title": title, "author": author, "createdAt": createdAt})
