from app import db

#création d'un model Friend
class Friend(db.Model):
    #définition des colonne de la table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    gender = db.Column(db.String(15), nullable=False)
    img_url = db.Column(db.String(200), nullable=True)
    
    #création d'un dictionnaire a l'aide des instances de Friends
    #pour pouvoir les transforme en json a l'aide jsonify de Flask
    def to_json(self):
        return {
            "id":self.id,
            "name":self.name,
            "role":self.role,
            "description":self.description,
            "gender":self.gender,
            "imgUrl":self.img_url
        }
    
