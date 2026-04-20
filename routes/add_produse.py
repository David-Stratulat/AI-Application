from flask import Blueprint, jsonify, request
from service import add_knowledge

add_bp = Blueprint('add', __name__)

@add_bp.route('/add_produs', methods=['POST'])
def add_produs():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    if not name or not price:
        return jsonify({"eroare": "Lipsesc date (nume sau pret)"})
    try:
        item = add_knowledge(name, price)
        return jsonify({
            "message": "Produsul a fost adăugat",
            "data": item
        }), 201
    except Exception as e: 
        return jsonify({"eroare": str(e)}),500