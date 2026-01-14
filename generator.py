import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ecoshop_db"]
products = db["products"]

# On vide la base avant de commencer pour éviter les doublons
products.delete_many({})

def populate():
    catalog = [
        {
            "nom": "PC Gamer Ultra",
            "categorie": "Electronique",
            "prix": 1500,
            "caracteristiques": {
                "cpu": "Intel i9",
                "ram": "32GB",
                "stockage": "1TB SSD"
            }
        },
        {
            "nom": "Jean Slim Fit",
            "categorie": "Mode",
            "prix": 60,
            "caracteristiques": {
                "taille": "M",
                "matiere": "Denim",
                "couleur": "Bleu"
            }
        },
        {
            "nom": "Château Margaux 2015",
            "categorie": "Alimentation",
            "prix": 450,
            "caracteristiques": {
                "annee": 2015,
                "region": "Bordeaux",
                "type": "Rouge"
            }
        }
    ]
    products.insert_many(catalog)
    print("✅ Catalogue généré avec succès !")

if __name__ == "__main__":
    populate()