from flask import Blueprint, render_template

bp = Blueprint('protein_alignment', __name__, url_prefix='/protein_alignment')

@bp.route('/')
def index():
    return render_template('protein-alignment.html')
