🚀 EcoShop : Gestion de Catalogue NoSQL Flexible
EcoShop est un projet de démonstration illustrant la puissance de MongoDB pour gérer un inventaire e-commerce hétérogène. Contrairement au SQL classique, ce système permet de stocker des produits aux caractéristiques totalement différentes sans changer la structure de la base.

🧐 Pourquoi MongoDB ? (Le choix technique)
Pour ce projet, nous avons utilisé MongoDB pour répondre à deux problématiques majeures du e-commerce :

Polymorphisme des données : Un ordinateur possède un CPU et de la RAM, tandis qu'une bouteille de vin possède une région et une année. MongoDB permet de stocker ces produits dans une seule collection (products) sans colonnes vides (NULL).

Puissance d'Analyse : Nous utilisons le Framework d'Agrégation pour calculer des statistiques (prix moyen par catégorie) directement sur le serveur de base de données.

📂 Structure du Projet
test_connection.py : Vérifie la liaison entre Python et MongoDB.

generator.py : Peuple la base avec des produits variés (Électronique, Mode, Alimentaire).

check_db.py : Affiche les données brutes pour prouver la flexibilité du schéma.

analyser.py : Réalise des calculs statistiques et des filtres avancés.

🛠️ Installation et Lancement
1. Prérequis
Python 3.x

MongoDB Community Server (installé et lancé localement)

2. Configuration
Ouvrez votre terminal dans le dossier du projet :

Bash

# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement (Windows)
venv\Scripts\activate

# Installer les dépendances
pip install pymongo dnspython
3. Exécution (Ordre de démonstration)
Suivez cet ordre pour la présentation :

Tester la connexion : python test_connection.py

Remplir la base : python generator.py

Visualiser les données : python check_db.py

Lancer l'analyse : python analyser.py

🎯 Conclusion
Ce projet montre que l'utilisation d'une base NoSQL comme MongoDB offre une agilité incomparable. Nous pouvons ajouter de nouvelles catégories de produits (ex: Livres, Voitures) instantanément sans aucune migration de base de données, ce qui rend l'application extrêmement évolutive.