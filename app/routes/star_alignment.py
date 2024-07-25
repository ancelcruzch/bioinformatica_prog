from flask import Blueprint, render_template

bp = Blueprint('star_alignment', __name__, url_prefix='/star_alignment')

@bp.route('/')
def index():
    return render_template('star-alignment.html')
