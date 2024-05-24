import numpy as np

from blosum62 import blosum62


def local_alignment(seq1, seq2, gap_penalty):
    len1, len2 = len(seq1), len(seq2)

    # Ініціалізація матриць для оцінок та трасування
    score_matrix = np.zeros((len1 + 1, len2 + 1))
    traceback_matrix = np.zeros((len1 + 1, len2 + 1))

    # Змінні для відстеження максимального рахунку та його позиції
    max_score = 0
    max_i, max_j = 0, 0

    # Заповнення матриці оцінок
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            match = score_matrix[i - 1][j - 1] + blosum62[seq1[i - 1]][seq2[j - 1]]
            delete = score_matrix[i - 1][j] + gap_penalty
            insert = score_matrix[i][j - 1] + gap_penalty
            score_matrix[i][j] = max(0, match, delete, insert)

            # Визначення напрямку трасування
            if score_matrix[i][j] == match:
                traceback_matrix[i][j] = 1
            elif score_matrix[i][j] == delete:
                traceback_matrix[i][j] = 2
            elif score_matrix[i][j] == insert:
                traceback_matrix[i][j] = 3

            # Оновлення максимального рахунку та його позиції
            if score_matrix[i][j] > max_score:
                max_score = score_matrix[i][j]
                max_i, max_j = i, j

    # Трасування для отримання вирівняних послідовностей
    aligned_seq1, aligned_seq2 = '', ''
    i, j = max_i, max_j
    while i > 0 and j > 0 and score_matrix[i][j] > 0:
        if traceback_matrix[i][j] == 1:
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            i -= 1
            j -= 1
        elif traceback_matrix[i][j] == 2:
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = '-' + aligned_seq2
            i -= 1
        else:
            aligned_seq1 = '-' + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            j -= 1

    return aligned_seq1, aligned_seq2, max_score


# Тестування функції на прикладі
seq1 = "AKVSKS"
seq2 = "RVSKKT"
gap_penalty = 8
aligned_seq1, aligned_seq2, alignment_score = local_alignment(seq1, seq2, gap_penalty)

# Вивід результатів
print("--" * 20)
print("Input Sequence 1: ", seq1)
print("Input Sequence 2: ", seq2)
print("--" * 20)

print("Local alignment score:", alignment_score)
print("Local alignment:")
print("Sequence 1:", aligned_seq1)
print("Sequence 2:", aligned_seq2)
print("--" * 20)
