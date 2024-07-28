from flask import Blueprint, render_template, request

from app.utils.sequences.sequences import convertir_adn_a_arn, tipo_secuencia

bp = Blueprint('sequences', __name__, url_prefix='/sequences')

@bp.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        secuencia = request.form['secuencia']
        cantidad = len(secuencia)
        tipo = tipo_secuencia(secuencia)
        arn = ''
        if(tipo=='ADN'):
            arn = convertir_adn_a_arn(secuencia)

        resultado = {
            'cantidad': cantidad,
            'tipo': tipo,
            'arn': arn
        }


    return render_template('sequences.html', result=resultado)
