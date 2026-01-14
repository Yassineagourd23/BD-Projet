import pymongo
from pprint import pprint

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ecoshop_db"]

print("--- CONTENU DE LA BASE ECOSHOP ---")
tous_les_produits = db.products.find()

for p in tous_les_produits:
    print(f"\nProduit : {p['nom']}")
    pprint(p)