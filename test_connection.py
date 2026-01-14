import pymongo

def test():
    try:
        # Connexion locale par défaut
        client = pymongo.MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=2000)
        client.admin.command('ping')
        print("✅ Connexion réussie à MongoDB ! Le serveur répond.")
    except Exception as e:
        print(f"❌ Erreur : Impossible de se connecter. Vérifie que MongoDB est bien lancé.")
        print(f"Détails : {e}")

if __name__ == "__main__":
    test()