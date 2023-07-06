import os
from flask import Flask, request, jsonify
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

application = Flask(__name__)

application.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_HOSTNAME'] + ':27017/mydatabase'
mongo = PyMongo(application)


collection = mongo.db['users']


#route test
@application.route('/bonjour', methods=['GET'])
def hello_world():
    return 'Hello World!'

# print all database, the READ of CRUD
@application.route('/showusers', methods=['GET'])
def get_users():

    myusers = collection.find()

    user_list = []

    for user in myusers:

        user_list.append({'id': user['id'], 'name': user['name'], 'email': user['email']})

    return jsonify({'users': user_list})

@application.route('/newuser')
def create_user():

    user_data = {
        'id': request.args.get('id'),
        'name': request.args.get('name'),
        'email': request.args.get('email')}

    collection.insert_one(user_data)

    return jsonify({'message': 'User created successfully'})



if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000, debug=True)