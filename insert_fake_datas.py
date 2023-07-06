import os
from pymongo import MongoClient

def stock_in_db():

    MONGO_URI= 'mongodb://' + os.environ['MONGODB_HOSTNAME'] + ':27017/'

    client = MongoClient(MONGO_URI)
    db = client.get_database('mydatabase')

    collection = db.get_collection('users')

    # Liste des utilisateurs de base (données fictives pour cet exemple)
    users = [
        {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
        {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
        {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com'}
        ]   

    # Insertion des données dans la base de données
    for user in users:
        collection.insert_one(user)

if __name__ == '__main__':
    stock_in_db()
    print('Fin du script')