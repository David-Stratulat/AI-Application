from flask import Flask, jsonify, request, Response
from service import get_knowledge, get_allKnowledge, add_knowledge
from exceptions import DuplicateException

app = Flask(__name__, template_folder="templates")

@app.route('/products', methods=['GET']) 
def get_products():
    content = get_allKnowledge() 
    if not content:
        return jsonify({"eroare": "Nu exista produse"})
    return jsonify(content)

@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    content = get_knowledge(product_id) #Extragem un produs din baza de date
    if not content:
        return jsonify({"eroare": "Produsul nu a fost gasit"})
    return jsonify(content)
    

@app.route('/add_product', methods=['POST'])
def add_product():
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"eroare": "JSON invalid"}), 400

    try:
        name = data.get('name')
        price = data.get('price')

        if not name or not price:
            return jsonify({"eroare": "Lipsesc date"}), 400

        item = add_knowledge(name, price)
        return jsonify({"message": "Produs adăugat", "data": item}), 201

    except DuplicateException as e:
        return jsonify({"eroare": str(e)}), 409

    except Exception as e:
        return jsonify({"eroare": "Eroare internă"}), 500
    
@app.errorhandler(Exception)
def handle_exception(e):
     return jsonify({"eroare": "Eroare internă neprevăzută"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)




