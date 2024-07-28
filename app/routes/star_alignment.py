from flask import Blueprint, render_template, request

bp = Blueprint('star_alignment', __name__, url_prefix='/star_alignment')

@bp.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':

        nro_secuencias = request.form['num_sequences']
        resultado = {
            'demo_' : nro_secuencias
        }


    return render_template('star-alignment.html', result=resultado)
