from flask import Blueprint, render_template, request

from app.utils.simple_linkage.simple_linkage import read_matrix, minimum_distance

bp = Blueprint('simple_linkage', __name__, url_prefix='/simple_linkage')

@bp.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        input_text = request.form.get('matrix_input')
        if input_text:
            matrix, labels = read_matrix(input_text)
            print(matrix)
            print(labels)
            print(type(input_text))
        else:
            return "matrix_input is missing!", 400
        

    return render_template('simple-linkage.html', result=resultado)
