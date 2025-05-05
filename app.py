from flask import Flask
from config import Config
from extensions import db, login_manager
from models import User, Product

from blueprints.main.routes import main_bp
from blueprints.auth.routes import auth_bp
from blueprints.products.routes import products_bp
from blueprints.cart.routes import cart_bp
from blueprints.user.routes import user_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_first_request
def create_tables():
    db.create_all()

app.register_blueprint(main_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(cart_bp, url_prefix='/cart')
app.register_blueprint(user_bp, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)
