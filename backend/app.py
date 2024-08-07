from flask import Flask
from extentions import db, migrate, cors
from api.routes.friend.route_friend import *
from models import *

from api.routes.friend.route_friend import *
# Enregistre les gestionnaires d'erreurs personnalisés
from api.middlewares.error.middleware_error import handle_validation_error, handle_not_found_error, handle_generic_error
from api.middlewares.error.middleware_error import ValidationError, NotFoundError

app = Flask(__name__)
cors(app)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends.db'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = db(app)
migrate = migrate(app, db)

app.register_error_handler(ValidationError, handle_validation_error)
app.register_error_handler(NotFoundError, handle_not_found_error)
app.register_error_handler(Exception, handle_generic_error)



with app.app_context(): 
    db.create_all() #création de la base de donnée

#app.register_error_handler(ValidationError, handle_validation_error)
#app.register_error_handler(NotFoundError, handle_not_found_error)
#app.register_error_handler(Exception, handle_generic_error)

if __name__ == "__main__":
    app.run(debug=True)