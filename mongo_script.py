from pymongo import MongoClient

uri = "mongodb+srv://Chayun:Cykmongo30312@cluster0.j3hiewj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["zqj2mn"]
collection = db["favorites"]

docs = [
    {"item": "instagram", "category": "social", "rank": 1},
    {"item": "spotify", "category": "music", "rank": 2},
    {"item": "matcha latte", "category": "drink", "rank": 3},
    {"item": "tennis", "category": "sport", "rank": 4},
    {"item": "laptop", "category": "tech", "rank": 5}
]
collection.insert_many(docs)

print("Top 3 items:")
for doc in collection.find().limit(3):
    print(doc)
