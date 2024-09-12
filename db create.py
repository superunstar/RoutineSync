import sqlite3

# Connexion à la base de données (création si elle n'existe pas)
conn = sqlite3.connect('database.db')

# Création d'un curseur pour exécuter des commandes SQL
cur = conn.cursor()

# Création d'une table
cur.execute('''
    CREATE TABLE IF NOT EXISTS utilisateurs (
        nom TEXT NOT NULL
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS taches (
        tache TEXT NOT NULL
    )
''')

# Sauvegarder les modifications et fermer la connexion
conn.commit()
conn.close()
