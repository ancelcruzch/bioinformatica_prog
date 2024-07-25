from flask import Blueprint, render_template

bp = Blueprint('simple_linkage', __name__, url_prefix='/simple_linkage')

@bp.route('/')
def index():
    return render_template('simple-linkage.html')
