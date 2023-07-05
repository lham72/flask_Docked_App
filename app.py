from flask import Flask, render_template, request, redirect

 

app = Flask(__name__)

 

# Liste des utilisateurs (données fictives pour cet exemple)
users = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
    {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com'}
]

 

@app.route('/')
def home():
    return "Bonjour"

 
@app.route('/showuser')
def show():
    return "au revoir !"



 

if __name__ == '__main__':
    app.run(debug=True)