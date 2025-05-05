from flask import Blueprint, session, render_template, redirect, url_for, flash
from models import Product
from flask_login import login_required

cart_bp = Blueprint('cart', __name__, template_folder='templates')

@cart_bp.route('/')
def cart():
    data = session.get('cart', {})
    items = [(Product.query.get(int(pid)), qty) for pid, qty in data.items()]
    total = sum(p.price*qty for p,qty in items if p)
    return render_template('cart.html', items=items, total=total)

@cart_bp.route('/add/<int:product_id>')
def add_to_cart(product_id):
    data = session.get('cart', {})
    data[str(product_id)] = data.get(str(product_id),0)+1
    session['cart'] = data
    flash('Добавлено','success')
    return redirect(url_for('cart.cart'))

@cart_bp.route('/checkout')
@login_required
def checkout():
    session['cart'] = {}
    flash('Заказ оформлен','success')
    return redirect(url_for('main.index'))
