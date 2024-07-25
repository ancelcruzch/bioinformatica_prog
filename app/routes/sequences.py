from flask import Blueprint, render_template

bp = Blueprint('sequences', __name__, url_prefix='/sequences')

@bp.route('/')
def index():
    return render_template('sequences.html')
