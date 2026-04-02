from flask import Flask, jsonify, request, Response
from service import get_knowledge, get_allKnowledge, add_knowledge
from exceptions import DuplicateException

app = Flask(__name__, template_folder="templates")

@app.route('/products', methods=['GET']) 
def get_products():
    content = get_allKnowledge() #Extragem continutul din baza de date
    if not content:
        return jsonify({"eroare": "Nu exista produse"})
    return jsonify(content)

@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    content = get_knowledge(product_id) #Extragem un produs din baza de date
    if not content:
        return jsonify({"eroare": "Produsul nu a fost gasit"})
    return jsonify(content)
    

@app.route('/add_product/', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    if not name or not price:
        return jsonify({"eroare": "Lipsesc date (nume sau pret)"}), 400
    try: #Exception handling, blocul de cod "asculta" exceptii(erori) si returneaza in functie de eroare
        item = add_knowledge(name, price)
        return jsonify({
            "message": "Produsul a fost adăugat",
            "data": item
        }), 201
    except DuplicateException as e: #Nu se mai returneaza obiectul, ci doar eroarea
        return jsonify({"eroare": str(e)}), 409

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)




