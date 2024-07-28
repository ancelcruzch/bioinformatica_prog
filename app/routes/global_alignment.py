from flask import Blueprint, render_template, request

from app.utils.global_alignment.global_alignment import convert_to_uppercase, global_seq

bp = Blueprint('global_alignment', __name__, url_prefix='/global_alignment')


# Define la función para obtener la clase CSS correspondiente a un nucleótido
def get_nucleotide_class(nucleotide):
    # ADN
    if nucleotide == 'A':
        return 'A'
    elif nucleotide == 'T':
        return 'T'
    elif nucleotide == 'G':
        return 'G'
    elif nucleotide == 'C':
        return 'C'

    # ARN
    elif nucleotide == 'U':
        return 'U'
    
    # Gaps
    elif nucleotide == '-':
        return 'gap'

    # Aminoácidos
    elif nucleotide == 'R':
        return 'R'
    elif nucleotide == 'N':
        return 'N'
    elif nucleotide == 'D':
        return 'D'
    elif nucleotide == 'Q':
        return 'Q'
    elif nucleotide == 'E':
        return 'E'
    elif nucleotide == 'H':
        return 'H'
    elif nucleotide == 'I':
        return 'I'
    elif nucleotide == 'L':
        return 'L'
    elif nucleotide == 'K':
        return 'K'
    elif nucleotide == 'M':
        return 'M'
    elif nucleotide == 'F':
        return 'F'
    elif nucleotide == 'P':
        return 'P'
    elif nucleotide == 'S':
        return 'S'
    elif nucleotide == 'T':
        return 'T'
    elif nucleotide == 'W':
        return 'W'
    elif nucleotide == 'Y':
        return 'Y'
    elif nucleotide == 'V':
        return 'V'
    elif nucleotide == 'B':
        return 'B'
    elif nucleotide == 'Z':
        return 'Z'
    elif nucleotide == 'X':
        return 'X'
    else:
        return 'unknown'


@bp.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        secuencia1 = request.form['secuencia1']
        secuencia2 = request.form['secuencia2']

        secuencia1 = convert_to_uppercase(secuencia1)
        secuencia2 = convert_to_uppercase(secuencia2)

        match = int(request.form['match'])
        mismatch = int(request.form['mismatch'])
        gap = int(request.form['gap'])

        alineamientos = global_seq(secuencia1,secuencia2, match, mismatch, gap)
        
        resultado = {
            'alignments': alineamientos
        }

    return render_template('global-alignment.html', result=resultado)


# Pasa la función a la plantilla
@bp.app_context_processor
def utility_processor():
    return dict(get_nucleotide_class=get_nucleotide_class)