from flask import Blueprint, render_template

bp = Blueprint('complete_linkage', __name__, url_prefix='/complete_linkage')

@bp.route('/')
def index():
    return render_template('complete-linkage.html')
