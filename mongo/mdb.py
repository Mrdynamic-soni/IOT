from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/")

mydb = myclient["sensor"]

mycol = mydb["values"]

data = {"name":"dht11","temperature":23.6,"humidity":56.2}

new_data = mycol.insert_one(data)


print(mydb.list_collection_names())

print(new_data.inserted_id)

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

new_dat = mycol.insert_many(mylist)

print(new_dat.inserted_ids)

for x in mycol.find():
  print(x)