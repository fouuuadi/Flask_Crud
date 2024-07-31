from app import app, db  
from flask import request, jsonify 
from models import Friend

@app.route("/api/friends",methods=["GET"])
def get_friends():
    friends = Friend.query.all() #récupère tout les champs de la table Friend (Model Friend)
    result = [friend.to_json() for friend in friends] # récupère le dictionnaire pour le parcourir
    return jsonify(result), 200 

#création d'un friend
@app.route("/api/friends", methods=["POST"])
def create_friend():
    try:
        data = request.json
        
        name = data.get("name")
        role = data.get("role")
        description = data.get("description")
        gender = data.get("gender")#genre
        
        # Fetch avatar image basee sur ton genre
        if gender == "male":
            img_url = f"https://avatar.iran.liara.run/public/boy?username={name}"
        elif gender == "female":
            img_url = f"https://avatar.iran.liara.run/public/girl?username={name}"
        else:
            img_url = None
            
        new_friend = Friend(name=name, role=role, description=description, gender=gender, img_url=img_url)
            
        db.session.add(new_friend)    
        db.session.commit()
            
        return jsonify({"msg":"Friend created successfully"}),201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}),500