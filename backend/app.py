from flask import Flask
from extentions import db, migrate, cors
from api.routes.friend.route_friend import route_friend
from models import *
# Enregistre les gestionnaires d'erreurs personnalisés
from api.middlewares.error.middleware_error import handle_validation_error, handle_not_found_error, handle_generic_error
from api.middlewares.error.middleware_error import ValidationError, NotFoundError

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialiser les extensions avec l'application
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    # Enregistrer les gestionnaires d'erreurs
    app.register_error_handler(ValidationError, handle_validation_error)
    app.register_error_handler(NotFoundError, handle_not_found_error)
    app.register_error_handler(Exception, handle_generic_error)

    # Enregistrer les blueprints
    app.register_blueprint(route_friend)

    # Créer les tables de la base de données
    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
