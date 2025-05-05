from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from models import User
from extensions import db

auth_bp = Blueprint('auth', __name__, template_folder='templates')

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        u = request.form['username']
        p = request.form['password']
        user = User.query.filter_by(username=u).first()
        if not user or not check_password_hash(user.password_hash, p):
            flash('Неверные данные','error')
            return redirect(url_for('auth.login'))
        login_user(user)
        return redirect(url_for('main.index'))
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        u = request.form['username']
        e = request.form['email']
        p = request.form['password']
        if User.query.filter((User.username==u)|(User.email==e)).first():
            flash('Пользователь существует','error')
            return redirect(url_for('auth.register'))
        new = User(username=u, email=e, password_hash=generate_password_hash(p))
        db.session.add(new)
        db.session.commit()
        flash('Успех','success')
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
