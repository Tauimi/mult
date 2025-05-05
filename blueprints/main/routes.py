from flask import Blueprint, render_template
from flask_login import current_user

main_bp = Blueprint('main', __name__, template_folder='templates')

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/contact')
def contact():
    return render_template('contact.html')

@main_bp.route('/faq')
def faq():
    return render_template('faq.html')

@main_bp.route('/gallery')
def gallery():
    return render_template('gallery.html')
