from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from .models import Product
from . import db
import json
import requests
from flask import Blueprint, render_template, request, jsonify, current_app

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

@views.route('/search')
def search():
    query = request.args.get('q', '').lower()
    if query:
        products = Product.query.filter(Product.name.ilike(f'%{query}%')).all()
    else:
        products = Product.query.all()

    product_list = [{
        "name": product.name,
        "price": product.price,
        "calories": product.calories,
        "protein": product.protein,
        "fat": product.fat,
        "carbs": product.carbs,
        "fiber": product.fiber
    } for product in products]
    
    return jsonify(product_list)

@views.route('/find_recipes', methods=['GET'])
def find_recipes():
    selected_products = request.args.getlist('products')  # Pobierz produkty z listy
    query = ','.join(selected_products)  # Połącz produkty w jedno zapytanie

    # Przygotuj zapytanie do API Edamam
    app_id = current_app.config['EDAMAM_APP_ID']
    app_key = current_app.config['EDAMAM_APP_KEY']
    url = f'https://api.edamam.com/search?q={query}&app_id={app_id}&app_key={app_key}&to=5'

    response = requests.get(url)
    print(f"API URL: {url}")  # Debug: wyświetl zapytanie API
    print(f"Response Status Code: {response.status_code}")  # Debug: status kod odpowiedzi

    if response.status_code == 200:
        recipes = response.json().get('hits', [])
        if not recipes:
            print("No recipes found")  # Debug: brak wyników
        return jsonify([{
            'label': recipe['recipe']['label'],
            'url': recipe['recipe']['url'],
            'image': recipe['recipe']['image'],
            'dietLabels': recipe['recipe']['dietLabels'],
        } for recipe in recipes])
    else:
        print(f"Error: {response.text}")  # Debug: wyświetl treść błędu
        return jsonify({'error': 'Error fetching recipes from API'}), 500


