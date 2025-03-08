from src.models import db, User, Character, Planet
from app import app

# Criar contexto da aplicação
with app.app_context():
    # Criar utilizadores fictícios
    user1 = User(email="luke@starwars.com", password="force123", created_at="2025-03-07")
    user2 = User(email="vader@starwars.com", password="sithlord", created_at="2025-03-07")

    # Criar personagens
    char1 = Character(name="Luke Skywalker", birth_year="19BBY", gender="male", height="172", mass="77")
    char2 = Character(name="Darth Vader", birth_year="41.9BBY", gender="male", height="202", mass="136")

    # Criar planetas
    planet1 = Planet(name="Tatooine", climate="arid", terrain="desert", population="200000")
    planet2 = Planet(name="Hoth", climate="frozen", terrain="tundra, ice caves, mountain ranges", population="unknown")

    # Adicionar à sessão do SQLAlchemy
    db.session.add_all([user1, user2, char1, char2, planet1, planet2])

    # Confirmar as alterações
    db.session.commit()

    print("Base de dados populada com sucesso!")
