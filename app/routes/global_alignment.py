from flask import Blueprint, render_template, request

from app.utils.global_alignment.main import convert_to_uppercase, global_seq

bp = Blueprint('global_alignment', __name__, url_prefix='/global_alignment')

@bp.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        secuencia1 = request.form['secuencia1']
        secuencia2 = request.form['secuencia2']

        secuencia1 = convert_to_uppercase(secuencia1)
        secuencia2 = convert_to_uppercase(secuencia2)

        alineamientos = global_seq(secuencia1,secuencia2)
        
        resultado = {
            'alignments': alineamientos
        }

    return render_template('global-alignment.html', result=resultado)