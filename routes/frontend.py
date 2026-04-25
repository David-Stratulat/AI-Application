from flask import Blueprint, render_template

frontend_bp = Blueprint('frontend', __name__)

@frontend_bp.route('/')
def index():
    return render_template('index.html')

@frontend_bp.route('/pagina/produse')
def pagina_produse():
    return render_template('produse.html')

@frontend_bp.route('/pagina/cauta')
def pagina_cauta():
    return render_template('cauta.html')

@frontend_bp.route('/pagina/add_produs')
def pagina_adauga():
    return render_template('adauga.html')

@frontend_bp.route('/pagina/update_produs')
def pagina_update():
    return render_template('update.html')