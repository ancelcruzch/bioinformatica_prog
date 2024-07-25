from flask import Blueprint, render_template

bp = Blueprint('point_matrix', __name__, url_prefix='/point_matrix')

@bp.route('/')
def index():
    return render_template('point-matrix.html')
