from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends.db'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import routes

with app.app_context(): 
    db.create_all() #création de la base de donnée

if __name__ == "__main__":
    app.run(debug=True)