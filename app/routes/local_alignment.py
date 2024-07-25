from flask import Blueprint, render_template

bp = Blueprint('local_alignment', __name__, url_prefix='/local_alignment')

@bp.route('/')
def index():
    return render_template('local-alignment.html')
