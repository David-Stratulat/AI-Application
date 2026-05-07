from flask import Blueprint, jsonify, request
from service import get_allKnowledge, get_product_by_id, get_product_by_name

view_bp = Blueprint('view_produse', __name__)

@view_bp.route('/produse', methods=['GET']) 
def get_produse():
    try:
        content = get_allKnowledge()
        if not content:
            return jsonify({"eroare": "Nu exista produse"})
        return jsonify(content)
    except Exception as e:
        return jsonify({"eroare": str(e)}), 500

@view_bp.route('/produs/<int:produs_id>', methods=['GET'])
def get_produs(produs_id):
    try:
        content = get_product_by_id(produs_id) 
        if not content:

            return jsonify({"eroare": "Produsul nu a fost gasit", "status": 404}), 404
        return jsonify(content)
    
    except Exception as e:
        return jsonify({"eroare": str(e), "status": 500}), 500
    
@view_bp.route('/produs/nume/<string:name>', methods=['GET'])
def get_produs_dupa_nume(name):
    try:
        produse = get_product_by_name(name)

        if not produse:
            return jsonify({
                "eroare": "Nu exista produse cu acest nume"
            }), 404

        return jsonify(produse)

    except Exception as e:
        return jsonify({
            "eroare": str(e)
        }), 500