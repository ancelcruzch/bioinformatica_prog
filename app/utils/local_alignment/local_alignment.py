import numpy as np

def convert_to_uppercase(s):
    return s.upper()

def smith_waterman(seq1, seq2, match_score=1, mismatch_penalty=-1, gap_penalty=-2):
    m, n = len(seq1), len(seq2)
    # Inicializar matrices de puntuación y trazado
    score_matrix = np.zeros((m + 1, n + 1))
    traceback_matrix = np.zeros((m + 1, n + 1))

    # Rellenar matrices
    max_score = 0
    max_pos = None
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = score_matrix[i - 1, j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_penalty)
            delete = score_matrix[i - 1, j] + gap_penalty
            insert = score_matrix[i, j - 1] + gap_penalty
            score_matrix[i, j] = max(0, match, delete, insert)
            
            if score_matrix[i, j] == 0:
                traceback_matrix[i, j] = 0
            elif score_matrix[i, j] == match:
                traceback_matrix[i, j] = 1
            elif score_matrix[i, j] == delete:
                traceback_matrix[i, j] = 2
            elif score_matrix[i, j] == insert:
                traceback_matrix[i, j] = 3
            
            if score_matrix[i, j] >= max_score:
                max_score = score_matrix[i, j]
                max_pos = (i, j)

    def traceback(start_pos):
        aligned_seq1 = []
        aligned_seq2 = []
        i, j = start_pos
        while traceback_matrix[i, j] != 0:
            if traceback_matrix[i, j] == 1:
                aligned_seq1.append(seq1[i - 1])
                aligned_seq2.append(seq2[j - 1])
                i -= 1
                j -= 1
            elif traceback_matrix[i, j] == 2:
                aligned_seq1.append(seq1[i - 1])
                aligned_seq2.append('-')
                i -= 1
            elif traceback_matrix[i, j] == 3:
                aligned_seq1.append('-')
                aligned_seq2.append(seq2[j - 1])
                j -= 1
        return ''.join(reversed(aligned_seq1)), ''.join(reversed(aligned_seq2))

    alignments = []
    for i in range(m + 1):
        for j in range(n + 1):
            if score_matrix[i, j] == max_score:
                alignments.append(traceback((i, j)))

    for align1, align2 in alignments:
        print(f"Alignment 1: {align1}")
        print(f"Alignment 2: {align2}")
        print()

    print(f"Score maximo local: {max_score}")
    return alignments, max_score

def main():
    # Ejemplo de uso
    seq1 = "GATTACA"
    seq2 = "GCATGCU"
    smith_waterman(seq1, seq2)
