from flask import Blueprint, render_template, request

bp = Blueprint('point_matrix', __name__, url_prefix='/point_matrix')

@bp.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        secuencia1 = request.form['secuencia1']
        secuencia2 = request.form['secuencia2']
        demo = len(secuencia1)
        resultado = {
            'demo_' : demo
        }

    return render_template('point-matrix.html', result=resultado)
