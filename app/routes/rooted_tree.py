from flask import Blueprint, render_template

bp = Blueprint('rooted_tree', __name__, url_prefix='/rooted_tree')

@bp.route('/')
def index():
    return render_template('rooted-tree.html')
