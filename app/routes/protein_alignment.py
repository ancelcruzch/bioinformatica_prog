from flask import Blueprint, render_template

bp = Blueprint('protein_alignment', __name__, url_prefix='/protein')

@bp.route('/')
def index():
    return render_template('protein_alignment.html')
