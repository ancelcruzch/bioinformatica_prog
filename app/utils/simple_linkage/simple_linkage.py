import numpy as np

input_text = """
0
10.387561       0
17.558267      20.305233       0
19.330544       24.120915     17.941590       0
"""

# Declarar variables globales
global_matrix = []
global_labels = []

def read_matrix(input_text):
    global global_matrix, global_labels
    global_matrix = []  # Inicializar como lista vacía
    global_labels = []  # Inicializar como lista vacía
    
    lines = input_text.strip().split('\n')
    max_cols = 0
    for line in lines:
        row = [float(value) for value in line.split()]
        global_matrix.append(row)
        if len(row) > max_cols:
            max_cols = len(row)
    
    # Asegurarse de que la matriz sea cuadrada agregando ceros si es necesario
    for row in global_matrix:
        while len(row) < max_cols:
            row.append(0.0)  # Agregar ceros hasta que tenga el mismo número de columnas que max_cols
    
    # Generar etiquetas para cada fila
    for i in range(len(global_matrix)):
        index_label = chr(ord('A') + i)
        global_labels.append(index_label)
    return global_matrix, global_labels

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print()

def make_symmetrical(matrix):
    lower_triangle = np.tril(matrix)
    symmetrical_matrix = lower_triangle + lower_triangle.T - np.diag(np.diag(lower_triangle))
    return symmetrical_matrix

class MatrixWithLabels:
    def __init__(self, matrix=None, labels=None):
        # Si matrix o labels no se proporcionan, se inicializan como arrays vacíos.
        self.matrix = np.array(matrix) if matrix is not None else np.array([])
        self.labels = np.array(labels) if labels is not None else np.array([])

def modify_values(matrix, labels, pos1, pos2):
    pos_min = min(pos1,pos2)
    pos_max = max(pos1,pos2)
    matrix = np.delete(matrix,pos_max, axis=0)
    matrix = np.delete(matrix,pos_max, axis=1)
    nueva_cadena = labels[pos_min] + labels[pos_max]
    labels[pos_min] = nueva_cadena
    del labels[pos_max]
    print("kajsnfhsnfnjsk")
    print(matrix)
    print(labels)
    print("**************************************")
    print(global_matrix)

    return matrix, labels

def minimum_distance(matrix, labels):
    print("  DISTANCIA MINIMA    ")
    min_aux, index_f, index_c = find_min(matrix)
    matrix, labels = modify_values(matrix, labels, index_f, index_c)
    print(global_matrix)


def find_max(matrix):
    index_f = None
    index_c = None
    max_value = -np.inf
    n = matrix.shape[0]
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[j][i] > max_value:
                max_value = matrix[j][i]
                index_f = j
                index_c = i
    return max_value, index_f, index_c

def find_min(matrix):
    index_f = None
    index_c = None
    min_value = np.inf
    n = matrix.shape[0]
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[j][i] < min_value:
                min_value = matrix[j][i]
                index_f = j
                index_c = i
    return min_value, index_f, index_c

def main():
    global global_matrix, global_labels
    print(input_text)
    read_matrix(input_text)
    print(global_matrix)
    print(global_labels)
    print(type(global_matrix))
    global_matrix = np.array(global_matrix)
    global_labels = np.array(global_labels)
    print(type(global_matrix))
    print()
    #
    matrix = global_matrix.copy()



if __name__ == "__main__":
    main()
