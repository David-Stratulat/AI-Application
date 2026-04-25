from flask import Blueprint, request, jsonify
from service import update_knowledge

update_bp = Blueprint('update_produse', __name__)

@update_bp.route('/update/<int:produs_id>', methods=['POST'])
def update_produs(produs_id):
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "status": "error",
                "mesaj": "Request invalid (fara JSON)"
            }), 400

        pret = data.get('price')

        if pret is None:
            return jsonify({
                "status": "error",
                "mesaj": "Pret lipsa"
            }), 400

        
        try:
            pret = float(pret)
        except (ValueError, TypeError):
            return jsonify({
                "status": "error",
                "mesaj": "Pret invalid (trebuie sa fie numar)"
            }), 400

        
        if pret < 0:
            return jsonify({
                "status": "error",
                "mesaj": "Pretul nu poate fi negativ"
            }), 400
        
        rezultat = update_knowledge(produs_id, price=pret)


        if rezultat["status"] == "error":
            return jsonify({
                "status": "error",
                "mesaj": rezultat["message"]
            }), 400

        return jsonify({
            "status": "success",
            "mesaj": "Pret actualizat cu succes",
            "data": rezultat["data"]
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "mesaj": "Eroare interna server",
            "debug": str(e)  
        }), 500