from flask import Blueprint, render_template

bp = Blueprint('global_alignment', __name__, url_prefix='/global_alignment')

@bp.route('/')
def index():
    return render_template('global-alignment.html')
