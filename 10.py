from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
# Create Database
db = client["LocalDB"]
# Create Collection
places = db["places"]
# Clear old data
places.delete_many({})
# INSERT
places.insert_many([
    {"name": "Chennai Tech Supplies", "category": "Electronics", "rating": 4.5, "city": "Chennai"},
    {"name": "Marina Cafe", "category": "Food & Beverage", "rating": 4.8, "city": "Chennai"},
    {"name": "Velachery Books", "category": "Retail", "rating": 4.2, "city": "Chennai"},
    {"name": "Anna Electronics", "category": "Electronics", "rating": 4.7, "city": "Chennai"},
    {"name": "Beach Restaurant", "category": "Food & Beverage", "rating": 4.6, "city": "Chennai"}
])

# SELECT *
print("\n--- All Records ---")
for place in places.find():
    print(place)
# SELECT WHERE
print("\n--- Electronics Stores ---")
for place in places.find({"category": "Electronics"}):
    print(place)
# SELECT WHERE rating > 4.5
print("\n--- Highly Rated Places ---")
for place in places.find({"rating": {"$gt": 4.5}}):
    print(place)
# SELECT with LIMIT
print("\n--- First 2 Records ---")
for place in places.find().limit(2):
    print(place)
# ORDER BY rating DESC
print("\n--- Sorted by Rating ---")
for place in places.find().sort("rating", -1):
    print(place)

# COUNT
print("\nTotal Records:", places.count_documents({}))
# UPDATE
places.update_one(
    {"name": "Marina Cafe"},
    {"$set": {"rating": 4.9}}
)
print("\n--- Updated Marina Cafe ---")
print(places.find_one({"name": "Marina Cafe"}))
# UPDATE MANY
places.update_many(
    {"category": "Electronics"},
    {"$set": {"discount": "10%"}}
)
print("\n--- Electronics After Update Many ---")
for place in places.find({"category": "Electronics"}):
    print(place)

# DISTINCT
print("\nDistinct Categories:")
print(places.distinct("category"))
# CREATE INDEX
places.create_index("category")
# DELETE ONE
places.delete_one({"name": "Velachery Books"})
# DELETE MANY
places.delete_many({"rating": {"$lt": 4.6}})
print("\n--- Final Records ---")
for place in places.find():
    print(place)
# DROP COLLECTION (Optional)
# places.drop()
# DROP DATABASE (Optional)
# client.drop_database("LocalDB")
client.close()
