from app import db

#création d'un model User
class User(db.Model):
    #définition des colonnes de la table User
    id = db.Column(db.Interger, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    
    def to_json_user(self):
        return {
            "id":self.id,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "age":self.age,
            "user_email":self.user_email           
        }