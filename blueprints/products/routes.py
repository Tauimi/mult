from flask import Blueprint, render_template
from models import Product

products_bp = Blueprint('products', __name__, template_folder='templates')

@products_bp.route('/')
def products():
    return render_template('products.html', products=Product.query.all())

@products_bp.route('/<int:product_id>')
def product_detail(product_id):
    return render_template('product_detail.html', product=Product.query.get_or_404(product_id))
