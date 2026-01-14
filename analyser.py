import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ecoshop_db"]

def run_stats():
    print("📊 ANALYSE DU CATALOGUE\n")

    # 1. Prix moyen par catégorie (Agrégation)
    pipeline = [
        {"$group": {"_id": "$categorie", "prix_moyen": {"$avg": "$prix"}}}
    ]
    
    print("💰 Prix moyen par catégorie :")
    for r in db.products.aggregate(pipeline):
        print(f"- {r['_id']} : {r['prix_moyen']:.2f}€")

    # 2. Trouver les produits qui ont une 'taille' (Mode)
    print("\n👕 Articles avec une taille spécifiée :")
    for item in db.products.find({"caracteristiques.taille": {"$exists": True}}):
        print(f"- {item['nom']} (Taille: {item['caracteristiques']['taille']})")

if __name__ == "__main__":
    run_stats()