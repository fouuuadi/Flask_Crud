from app import app, db  
from flask import request, jsonify 
from models.friend import Friend

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
        
        required_fields = ["name","role","description","gender"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error":f'Missing required field; {field}'}),400
        
        name = data.get("name")
        role = data.get("role")
        description = data.get("description")
        gender = data.get("gender")#genre
        social_links = data.get("socialLinks", {})
        
        # fetch avatar image basee sur ton genre
        if gender == "male":
            img_url = f"https://avatar.iran.liara.run/public/boy?username={name}"
        elif gender == "female":
            img_url = f"https://avatar.iran.liara.run/public/girl?username={name}"
        else:
            img_url = None
            
        new_friend = Friend(name=name, role=role, description=description, gender=gender, img_url=img_url, social_links=social_links)
            
        db.session.add(new_friend)    
        db.session.commit()
            
        return jsonify({"msg":"Friend created successfully"}),201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}),500

# delete
@app.route("/api/friends/<int:id>",methods=["DELETE"])
def delete_friend(id):
    try:
        friend = Friend.query.get(id)
        if friend is None:
            return jsonify({"error":"Friend not found"}),404
        
        db.session.delete(friend)
        db.session.commit()
        return jsonify({"msg":"Friend deleted"}),200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)})

# modification d'un profil Friend
@app.route("/api/friends/<int:id>", methods=["PATCH"])
def update_friend(id):
    try:
        friend = Friend.query.get(id)
        if friend is None:
            return jsonify({"error": "Friend not found"}), 400
        
        data = request.json
        
        friend.name = data.get("name", friend.name)
        friend.role = data.get("role", friend.role)
        friend.description = data.get("description", friend.description)
        new_gender = data.get("gender", friend.gender)
        social_links = data.get("socialLinks", {})
        
        #print(f"Current gender: {friend.gender}, New gender: {new_gender}")
        
        if social_links is not None:
            friend.social_links = social_links
        
        if new_gender != friend.gender:
            friend.gender = new_gender
            if new_gender == "male":
                friend.img_url = f"https://avatar.iran.liara.run/public/boy?username={friend.name}"
            elif new_gender == "female":
                friend.img_url = f"https://avatar.iran.liara.run/public/girl?username={friend.name}"
            else:
                friend.img_url = None
            
            #print(f"Updated img_url: {friend.img_url}")
            #print(f"Updated img_url: {friend.social_links}")
        
        db.session.commit()
        return jsonify(friend.to_json()), 200
        
    except Exception as e:
        db.session.rollback()
        print(f"Error updating friend: {e}")
        return jsonify({"error": str(e)}), 500