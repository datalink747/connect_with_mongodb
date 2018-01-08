from pip._vendor.requests.status_codes import title
from pymongo import MongoClient, DESCENDING

# Connect to the MongoDB, change the connection string per your MongoDB environment
client = MongoClient('localhost', 27017)
#connect to database
db = client.sony.user
print(db)
#Data
mongo_data = {
    'title': 'Python and MongoDB11',
    'description': 'connect python with mongodb',
    'author': 'soussi1',
    'email': 'soussi.mohamed747@outlook.com',
    'id': '4'
}

#add data to database
result = db.insert_one(mongo_data) #or db.insert(mongo_data)
#check first data from mongodb
print('First Data: {1}'.format(db.inserted_id))
cursor = db.find().sort('title',DESCENDING)
for document in cursor:
    print(document)

# update data

mongo_data2 = {
    'title': 'tutorial Kotlin',
    'description': 'dev kotlin',
    'author': 'soussi mohamed',
    'email': 'soussi.mohamed747@gmail.com',
    'id':'4'
}


db.update({'id': '3'},mongo_data2)
#remove data

db.remove({'id':'3'})











