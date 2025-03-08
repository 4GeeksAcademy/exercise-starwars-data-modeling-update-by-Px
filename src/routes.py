from flask import Blueprint, jsonify, request
from src.models import db, User, Character, Planet, Favorite

api = Blueprint('api', __name__)

# GET all users
@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    print(f"Users found: {users}")  # Debug
    users_list = [{"id": user.id, "email": user.email} for user in users]
    print(f"User list: {users_list}")  # Debug
    return jsonify(users_list), 200

# POST users
@api.route('/users', methods=['POST'])
def add_user():
    data = request.json
    if not data or not all(key in data for key in ["email", "password", "created_at"]):
        return jsonify({"error": "All fields are required"}), 400

    # Check if email already exists
    existing_user = User.query.filter_by(email=data["email"]).first()
    if existing_user:
        return jsonify({"error": "Email is already in use!"}), 400

    new_user = User(
        email=data["email"],
        password=data["password"],
        created_at=data["created_at"]
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User successfully created!", "id": new_user.id}), 201

# DELETE user
@api.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User successfully deleted"}), 200

# GET all characters
@api.route('/characters', methods=['GET'])
def get_characters():
    print("Receiving GET request for /characters")
    characters = Character.query.all()
    print(f"Found {len(characters)} characters")
    characters_list = [{"id": char.id, "name": char.name, "birth_year": char.birth_year, "gender": char.gender, "height": char.height, "mass": char.mass} for char in characters]
    return jsonify(characters_list), 200

# POST new character
@api.route('/characters', methods=['POST'])
def add_character():
    data = request.json
    if not data or not all(key in data for key in ["name", "birth_year", "gender", "height", "mass"]):
        return jsonify({"error": "All fields are required"}), 400

    new_character = Character(
        name=data["name"],
        birth_year=data["birth_year"],
        gender=data["gender"],
        height=data["height"],
        mass=data["mass"]
    )
    db.session.add(new_character)
    db.session.commit()
    return jsonify({"message": "Character successfully created!", "id": new_character.id}), 201

# DELETE character
@api.route('/characters/<int:id>', methods=['DELETE'])
def delete_character(id):
    character = Character.query.get(id)
    if not character:
        return jsonify({"error": "Character not found"}), 404

    db.session.delete(character)
    db.session.commit()
    return jsonify({"message": "Character successfully deleted"}), 200

# GET all planets
@api.route('/planets', methods=['GET'])
def get_planets():
    planets = Planet.query.all()
    planets_list = [{"id": planet.id, "name": planet.name, "climate": planet.climate, "terrain": planet.terrain, "population": planet.population} for planet in planets]
    return jsonify(planets_list), 200

# POST new planet
@api.route('/planets', methods=['POST'])
def add_planet():
    data = request.json
    if not data or not all(key in data for key in ["name", "climate", "terrain", "population"]):
        return jsonify({"error": "All fields are required"}), 400

    new_planet = Planet(
        name=data["name"],
        climate=data["climate"],
        terrain=data["terrain"],
        population=data["population"]
    )
    db.session.add(new_planet)
    db.session.commit()
    return jsonify({"message": "Planet successfully created!", "id": new_planet.id}), 201

# DELETE planet
@api.route('/planets/<int:id>', methods=['DELETE'])
def delete_planet(id):
    planet = Planet.query.get(id)
    if not planet:
        return jsonify({"error": "Planet not found"}), 404

    db.session.delete(planet)
    db.session.commit()
    return jsonify({"message": "Planet successfully deleted"}), 200

# GET all favorites
@api.route('/favorites', methods=['GET'])
def get_favorites():
    favorites = Favorite.query.all()
    favorites_list = [{"id": fav.id, "user_id": fav.user_id, "character_id": fav.character_id, "planet_id": fav.planet_id} for fav in favorites]
    return jsonify(favorites_list), 200

# POST new favorite
@api.route('/favorites', methods=['POST'])
def add_favorite():
    data = request.json
    user_id = data.get("user_id")
    character_id = data.get("character_id")
    planet_id = data.get("planet_id")

    if not user_id or (not character_id and not planet_id):
        return jsonify({"error": "You must provide a user_id and either a character_id or a planet_id"}), 400

    new_favorite = Favorite(user_id=user_id, character_id=character_id, planet_id=planet_id)
    db.session.add(new_favorite)
    db.session.commit()

    return jsonify({"message": "Favorite successfully added!", "id": new_favorite.id}), 201

# DELETE favorite
@api.route('/favorites/<int:id>', methods=['DELETE'])
def delete_favorite(id):
    favorite = Favorite.query.get(id)
    if not favorite:
        return jsonify({"error": "Favorite not found"}), 404

    db.session.delete(favorite)
    db.session.commit()
    return jsonify({"message": "Favorite successfully deleted"}), 200
