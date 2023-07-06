from flask import Flask, render_template, request, redirect, jsonify
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

application = Flask(__name__)

application.config["MONGO_URI"] = 'mongodb://host.Docker.internal:27017/mymongodb'

mongo = PyMongo(application)
db = mongo.db

# Liste des utilisateurs de base (données fictives pour cet exemple)
users = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
    {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com'}
    ]

#route test
@application.route('/bonjour', methods=['GET'])
def hello_world():
    return 'Hello World!'

# print all database, the READ of CRUD
@application.route('/showusers', methods=['GET'])
def get_users():

    users = db.users.find()

    user_list = []

    for user in users:

        user_list.append({'id': user['id'], 'name': user['name'], 'email': user['email']})

    return jsonify({'users': user_list})

@application.route('/newuser', methods=['POST'])
def create_user():

    user_data = request.get_json()

    db.users.insert_one(user_data)

    return jsonify({'message': 'User created successfully'})



if __name__ == '__main__':
    

    # Insertion des données dans la base de données
    for user in users:
        db.users.insert_one(user)
        
    application.run(host='0.0.0.0', port=5000, debug=True)