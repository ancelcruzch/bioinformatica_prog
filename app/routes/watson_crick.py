from flask import Blueprint, render_template

bp = Blueprint('watson_crick', __name__, url_prefix='/watson_crick')

@bp.route('/')
def index():
    return render_template('watson-crick.html')
