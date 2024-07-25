from flask import Blueprint, render_template

bp = Blueprint('weighted_linkage', __name__, url_prefix='/weighted_linkage')

@bp.route('/')
def index():
    return render_template('weighted-linkage.html')
