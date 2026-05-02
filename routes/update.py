from flask import Blueprint, request, jsonify
from service import update_knowledge

update_bp = Blueprint('update_produse', __name__)

@update_bp.route('/update/<int:id_produs>', methods=['POST'])
def update_produs(id_produs):
    try:
        data = request.get_json()

        if not data:
            return jsonify({"status": 400, "eroare": "Request invalid (fara JSON)"}), 400

        pret = data.get("price")

        if pret is None:
            return jsonify({"status": 400, "eroare": "Pret lipsa"}), 400

        try:
            pret = float(pret)
        except:
            return jsonify({"status": 400, "eroare": "Pret invalid (trebuie sa fie numar)"}), 400

        if pret < 0:
            return jsonify({"status": 400, "eroare": "Pretul nu poate fi negativ"}), 400

        rezultat = update_knowledge(id=id_produs, price=pret)

        if rezultat["status"] == 400:
            return jsonify({
                "status": 400,
                "eroare": rezultat["eroare"]
            }), 400

        return jsonify({
            "status": 200,
            "mesaj": "Pret actualizat cu succes",
            "data": rezultat["data"]
        }), 200

    except Exception as e:
        return jsonify({
            "status": 500,
            "mesaj": "Eroare interna server",
            "debug": str(e)
        }), 500
