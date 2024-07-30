import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist, squareform

def read_matrix(input_text):
    lines = input_text.strip().split('\n')
    matrix = []
    max_length = 0
    for line in lines:
        row = list(map(float, line.split()))
        max_length = max(max_length, len(row))
        matrix.append(row)
    for row in matrix:
        row.extend([0] * (max_length - len(row)))
    matrix = np.array(matrix, dtype=float)
    matrix = np.maximum(matrix, matrix.T)
    np.fill_diagonal(matrix, 0)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print()

def encontrar_minima_distancia(matriz):
    matriz = np.array(matriz)
    np.fill_diagonal(matriz, np.inf)  # Evita considerar la diagonal
    idx_min = np.unravel_index(np.argmin(matriz), matriz.shape)
    distancia_minima = matriz[idx_min]
    return idx_min, distancia_minima

def numero_a_letra(numero):
    resultado = ''
    while numero >= 0:
        resultado = chr((numero % 26) + ord('A')) + resultado
        numero = numero // 26 - 1
    return resultado

def actualizar_matriz(matriz, par, estrategia):
    matriz = np.array(matriz)
    nueva_matriz = np.delete(matriz, par, axis=0)
    nueva_matriz = np.delete(nueva_matriz, par, axis=1)
    
    if estrategia == 'simple':
        nueva_fila = np.min(matriz[par, :], axis=0)
    elif estrategia == 'complete':
        nueva_fila = np.max(matriz[par, :], axis=0)
    elif estrategia == 'average':
        nueva_fila = np.mean(matriz[par, :], axis=0)
    
    nueva_fila = np.delete(nueva_fila, par)
    nueva_fila = np.append(nueva_fila, 0.0)
    
    nueva_matriz = np.vstack((nueva_matriz, nueva_fila[:-1]))
    nueva_columna = np.append(nueva_fila[:-1], 0.0).reshape(-1, 1)
    nueva_matriz = np.hstack((nueva_matriz, nueva_columna))

    return nueva_matriz.tolist()

def clustering(matriz, estrategia):
    clusters = [[numero_a_letra(i)] for i in range(len(matriz))]
    matriz_actual = np.array(matriz)
    resultado_clusters = [clusters.copy()]
    resultado_matrices = [matriz_actual.copy()]
    distancias_minimas = []

    while len(clusters) > 1:
        (i, j), distancia_minima = encontrar_minima_distancia(matriz_actual)
        nuevo_cluster = clusters[i] + clusters[j]
        
        clusters = [clusters[k] for k in range(len(clusters)) if k not in (i, j)]
        clusters.append(nuevo_cluster)
        
        matriz_actual = actualizar_matriz(matriz_actual, (i, j), estrategia)
        
        resultado_clusters.append(clusters.copy())
        resultado_matrices.append(matriz_actual.copy())
        distancias_minimas.append(distancia_minima)
    
    return resultado_clusters, distancias_minimas

def crear_dendograma(labels, unions, weights, tittle, filename):
    # Crear un diccionario para mapear etiquetas a índices
    label_to_index = {label[0]: idx for idx, label in enumerate(labels)}
    
    # Inicializar una matriz de distancias con valores grandes (infinito)
    n_labels = len(labels)
    distance_matrix = [[float('inf')] * n_labels for _ in range(n_labels)]
    
    # Asignar cero a la diagonal (distancia a sí mismo es cero)
    for i in range(n_labels):
        distance_matrix[i][i] = 0
    
    # Llenar la matriz de distancias con los pesos especificados
    for union, weight in zip(unions, weights):
        indices = [label_to_index[item] for item in union]
        for i in range(len(indices)):
            for j in range(i + 1, len(indices)):
                index_i = indices[i]
                index_j = indices[j]
                # Actualizar solo si el peso actual es menor (camino más corto)
                if weight < distance_matrix[index_i][index_j]:
                    distance_matrix[index_i][index_j] = weight
                    distance_matrix[index_j][index_i] = weight
    
    # Convertir la matriz de distancia completa a una forma condensada que linkage() necesita
    condensed_matrix = squareform(distance_matrix)
    
    # Usar 'complete' como método de linkage para este caso
    linked = linkage(condensed_matrix, 'complete')
    
    # Dibujar el dendrograma
    plt.figure(figsize=(10, 7))
    dendro = dendrogram(
        linked,
        labels=[label[0] for label in labels],
        orientation='top',
        above_threshold_color='grey'  # color común por encima del umbral de corte
    )
    
    # Añadir etiquetas de peso en cada unión con color negro
    ax = plt.gca()
    for i, d, c in zip(dendro['icoord'], dendro['dcoord'], dendro['color_list']):
        x = 0.5 * sum(i[1:3])
        y = d[1]
        if y > 0:  # Solo etiquetar si la altura de unión es mayor que cero
            ax.text(x, y, f"{y:.2f}", ha='center', va='bottom', color='black')
    
    plt.title(tittle)
    plt.xlabel('ETIQUETAS')
    plt.ylabel('DISTANCIAS')
    plt.savefig(filename+'.png')
    plt.close()

def generar_dendogramas(input_text):
    matriz = read_matrix(input_text)
    strategies = ['simple', 'complete', 'average']

    # Inicializar diccionarios para almacenar resultados
    results = {}
    min_distances = {}

    # Asignar resultados a cada estrategia en los diccionarios
    for strategy in strategies:
        results[strategy], min_distances[strategy] = clustering(matriz, strategy)

    distancias = ["Distancia Minima", "Distancia Maxima", "Distancia Ponderada"]

    # Pre-procesamiento para crear dendograma para 'simple' strategy como ejemplo
    labels = results['simple'][0]
    uniones = [cluster[-1] for cluster in results['simple'][1:]]

    # Imprimir resultados para cada estrategia
    i = 0
    for strategy in strategies:
        print(f"Resultados para la estrategia {strategy}:")
        labels = results[strategy][0]
        uniones = [cluster[-1] for cluster in results[strategy][1:]]
        print(f"Labels: {labels}")
        print(f"Uniones: {uniones}")
        print(f"Distancias mínimas: {min_distances[strategy]}")
        print('-' * 50)  # Separador para claridad
        crear_dendograma(labels, uniones, min_distances[strategy], distancias[i], strategy)
        i += 1

text = '''0
41.6214	0		
18.0477	36.185	0	
30.0218	24.6916	23.8391	0
'''

generar_dendogramas(text)