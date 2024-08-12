from flask import Flask
from src.main.routes.calculators import calc_route_bp

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your-secret-key'

app.register_blueprint(calc_route_bp)