from flask import Blueprint, render_template

bp = Blueprint('neighbor_joining', __name__, url_prefix='/neighbor_joining')

@bp.route('/')
def index():
    return render_template('neighbor-joining.html')
