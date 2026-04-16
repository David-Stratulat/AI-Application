from flask import Flask
from routes.add_product import add_bp
from routes.view_products import view_bp

app = Flask(__name__, template_folder="templates")
app.register_blueprint(add_bp)
app.register_blueprint(view_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)




