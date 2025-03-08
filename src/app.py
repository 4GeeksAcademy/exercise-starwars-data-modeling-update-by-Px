from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from src.models import db
from src.routes import api  # <- Correctly imports the Blueprint

app = Flask(__name__)
CORS(app)

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.abspath(os.path.join(BASE_DIR, '../instance/starwars.db'))}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(api, url_prefix='/api')  # <- Ensures the Blueprint is registered

@app.route('/')
def home():
    return {"message": "Star Wars API is running!"}

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
