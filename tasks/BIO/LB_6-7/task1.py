import numpy as np

from blosum62 import blosum62


# Визначаємо функцію глобального вирівнювання за допомогою матриці замін BLOSUM62 та штрафу за прогалини
def global_alignment(seq1, seq2, subst_matrix, gap_penalty):
    len1, len2 = len(seq1), len(seq2)

    # Ініціалізуємо матриці для зберігання оцінок та напрямків трасування
    score_matrix = np.zeros((len1 + 1, len2 + 1))
    traceback_matrix = np.zeros((len1 + 1, len2 + 1))

    # Заповнюємо перший рядок і стовпець матриці оцінок з урахуванням штрафів за прогалини
    for i in range(1, len1 + 1):
        score_matrix[i, 0] = score_matrix[i - 1, 0] + gap_penalty
    for j in range(1, len2 + 1):
        score_matrix[0, j] = score_matrix[0, j - 1] + gap_penalty

    # Заповнюємо решту матриці оцінок
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            match_score = score_matrix[i - 1, j - 1] + subst_matrix[seq1[i - 1]][seq2[j - 1]]
            delete_score = score_matrix[i - 1, j] + gap_penalty
            insert_score = score_matrix[i, j - 1] + gap_penalty
            score_matrix[i, j] = max(match_score, delete_score, insert_score)

            # Визначаємо напрямок трасування
            if score_matrix[i, j] == match_score:
                traceback_matrix[i, j] = 1
            elif score_matrix[i, j] == delete_score:
                traceback_matrix[i, j] = 2
            else:
                traceback_matrix[i, j] = 3

    # Трасування для побудови вирівняних послідовностей
    aligned_seq1, aligned_seq2 = [], []
    i, j = len1, len2
    while i > 0 or j > 0:
        if traceback_matrix[i, j] == 1:
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append(seq2[j - 1])
            i -= 1
            j -= 1
        elif traceback_matrix[i, j] == 2:
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append('-')
            i -= 1
        else:
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[j - 1])
            j -= 1

    # Перевертаємо вирівняні послідовності
    aligned_seq1.reverse()
    aligned_seq2.reverse()

    return ''.join(aligned_seq1), ''.join(aligned_seq2), score_matrix[len1, len2]


# Тестування функції з прикладами
seq1 = "AKVSK"
seq2 = "RVSKK"
gap_penalty = 8

aligned_seq1, aligned_seq2, alignment_score = global_alignment(seq1, seq2, blosum62, gap_penalty)

# Виводимо результати
print("--" * 20)
print("Input Sequence 1: ", seq1)
print("Input Sequence 2: ", seq2)
print("--" * 20)

print("Local alignment:")
print("Sequence 1:", aligned_seq1)
print("Sequence 2:", aligned_seq2)
print("Weight: ", alignment_score)
print("--" * 20)
