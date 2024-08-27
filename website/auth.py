from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, current_user, logout_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nickName = request.form.get('nickName')
        password = request.form.get('password')

        user = User.query.filter_by(nickName=nickName).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('User does not exist', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sing_up():
    if request.method == 'POST':
        nickName = request.form.get('nickName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(nickName=nickName).first()

        if user:
            flash('User already exist', category='error')
        elif len(nickName) < 3:
            flash('Your Nickname must be at least 4 characters long', category='error')
        elif password1 != password2:
            flash('Your second password is diffrent than first', category='error')
        elif len(password1) < 4:
            flash('Your password must be at least 4 characters long', category='error')
        else:
            new_user = User(nickName=nickName, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='succes')
            login_user(user)
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)

