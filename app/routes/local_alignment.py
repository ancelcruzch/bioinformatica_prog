from flask import Blueprint, render_template

bp = Blueprint('local_alignment', __name__, url_prefix='/local')

@bp.route('/')
def index():
    return render_template('local_alignment.html')
