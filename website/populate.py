from .models import Product, db
from . import create_app

def add_products():
    products = [
    {"name": "Raspberry", "price": 4.5, "calories": 52, "protein": 1.2, "fat": 0.6, "carbs": 12, "fiber": 6.5},
    {"name": "Avocado", "price": 2.5, "calories": 160, "protein": 2, "fat": 15, "carbs": 9, "fiber": 7},
    {"name": "Cucumber", "price": 0.9, "calories": 16, "protein": 0.7, "fat": 0.1, "carbs": 4, "fiber": 0.5},
    {"name": "Tomato", "price": 1.1, "calories": 18, "protein": 0.9, "fat": 0.2, "carbs": 4, "fiber": 1.2},
    {"name": "Potato", "price": 0.6, "calories": 77, "protein": 2, "fat": 0.1, "carbs": 17, "fiber": 2.2},
    {"name": "Spinach", "price": 2.0, "calories": 23, "protein": 2.9, "fat": 0.4, "carbs": 3.6, "fiber": 2.2},
    {"name": "Cauliflower", "price": 1.3, "calories": 25, "protein": 1.9, "fat": 0.3, "carbs": 5, "fiber": 2},
    {"name": "Chicken Breast", "price": 5.5, "calories": 165, "protein": 31, "fat": 3.6, "carbs": 0, "fiber": 0},
    {"name": "Salmon", "price": 8.0, "calories": 208, "protein": 20, "fat": 13, "carbs": 0, "fiber": 0},
    {"name": "Egg", "price": 0.2, "calories": 68, "protein": 6, "fat": 5, "carbs": 1, "fiber": 0},
    {"name": "Milk", "price": 1.2, "calories": 42, "protein": 3.4, "fat": 1, "carbs": 5, "fiber": 0},
    {"name": "Almond", "price": 12.0, "calories": 579, "protein": 21, "fat": 50, "carbs": 22, "fiber": 12.5},
    {"name": "Walnut", "price": 10.0, "calories": 654, "protein": 15, "fat": 65, "carbs": 14, "fiber": 6.7},
    {"name": "Brown Rice", "price": 1.8, "calories": 123, "protein": 2.7, "fat": 1, "carbs": 26, "fiber": 1.8},
    {"name": "Oats", "price": 2.0, "calories": 389, "protein": 16.9, "fat": 6.9, "carbs": 66, "fiber": 10.6},
    {"name": "Lentils", "price": 1.5, "calories": 116, "protein": 9, "fat": 0.4, "carbs": 20, "fiber": 7.9},
    {"name": "Chickpeas", "price": 2.2, "calories": 164, "protein": 8.9, "fat": 2.6, "carbs": 27, "fiber": 7.6},
    {"name": "Tofu", "price": 3.0, "calories": 144, "protein": 16, "fat": 8, "carbs": 2, "fiber": 2}
]


    for product_data in products:
        product = Product(**product_data)
        db.session.add(product)
    db.session.commit()

# Uruchomienie aplikacji w kontekście
app = create_app()

with app.app_context():
    add_products()
