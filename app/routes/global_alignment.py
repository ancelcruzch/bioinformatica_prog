from flask import Blueprint, render_template

bp = Blueprint('global_alignment', __name__, url_prefix='/global')

@bp.route('/')
def index():
    return render_template('global_alignment.html')
