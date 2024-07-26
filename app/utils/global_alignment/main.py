import time

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def convert_to_uppercase(s):
    return s.upper()

def traceback(matrix, seq1, seq2, i, j, aligned1, aligned2, match, mismatch, gap, alignments):
    if i == 0 and j == 0:
        alignments.append((aligned1[::-1], aligned2[::-1]))
        return
    if i > 0 and matrix[i][j] == matrix[i-1][j] + gap:
        traceback(matrix, seq1, seq2, i-1, j, aligned1 + seq1[i-1], aligned2 + '-', match, mismatch, gap, alignments)
    if j > 0 and matrix[i][j] == matrix[i][j-1] + gap:
        traceback(matrix, seq1, seq2, i, j-1, aligned1 + '-', aligned2 + seq2[j-1], match, mismatch, gap, alignments)
    if i > 0 and j > 0 and matrix[i][j] == matrix[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch):
        traceback(matrix, seq1, seq2, i-1, j-1, aligned1 + seq1[i-1], aligned2 + seq2[j-1], match, mismatch, gap, alignments)

def global_seq(seq1, seq2):
    match = 1
    mismatch = -1
    gap = -2
    n = len(seq1)
    m = len(seq2)
    matrix = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        matrix[i][0] = i * gap
    for j in range(m + 1):
        matrix[0][j] = j * gap

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diagonal = matrix[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch)
            up = matrix[i - 1][j] + gap
            left = matrix[i][j - 1] + gap
            matrix[i][j] = max(diagonal, up, left)

    print("Matriz de alineamiento:")
    print_matrix(matrix)

    alignments = []
    traceback(matrix, seq1, seq2, n, m, '', '', match, mismatch, gap, alignments)
    print("Alineamientos óptimos:")
    for first, second in alignments:
        print(first)
        print(second)
        print()
    return alignments

if __name__ == "__main__":
    start_time = time.time_ns()
    seq_a = "TCAAGCGTTAGAG"
    seq_b = "ATTAAAGGTTTAT"

    print("Secuencia 01:", seq_a)
    print("Secuencia 02:", seq_b)

    global_seq(seq_a, seq_b)
    end_time = time.time_ns()
    duration = end_time - start_time
    print("Tiempo de ejecución:", duration, "nanosegundos")
