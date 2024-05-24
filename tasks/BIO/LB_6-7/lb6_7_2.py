import numpy as np
from lb6_7_1 import blosum62  # Importing the blosum62 matrix from lb6_7_1 module


def local_alignment(seq1, seq2, gap_penalty):
    """
    Performs local alignment between two sequences using the Smith-Waterman algorithm.

    Args:
    - seq1 (str): The first sequence.
    - seq2 (str): The second sequence.
    - gap_penalty (int): The gap penalty value for sequence alignment.

    Returns:
    - aligned_seq1 (str): The aligned sequence 1.
    - aligned_seq2 (str): The aligned sequence 2.
    - alignment_score (int): The alignment score.
    """
    len_seq1, len_seq2 = len(seq1), len(seq2)
    score_matrix = np.zeros((len_seq1 + 1, len_seq2 + 1))
    traceback_matrix = np.zeros((len_seq1 + 1, len_seq2 + 1))
    max_score = 0
    max_i, max_j = 0, 0
    for i in range(1, len_seq1 + 1):
        for j in range(1, len_seq2 + 1):
            match = score_matrix[i - 1][j - 1] + blosum62[seq1[i - 1]][seq2[j - 1]]
            delete = score_matrix[i - 1][j] + gap_penalty
            insert = score_matrix[i][j - 1] + gap_penalty
            score_matrix[i][j] = max(0, match, delete, insert)
            if score_matrix[i][j] == match:
                traceback_matrix[i][j] = 1  # Diagonal arrow representing match
            elif score_matrix[i][j] == delete:
                traceback_matrix[i][j] = 2  # Up arrow representing deletion
            elif score_matrix[i][j] == insert:
                traceback_matrix[i][j] = 3  # Left arrow representing insertion
            if score_matrix[i][j] > max_score:
                max_score = score_matrix[i][j]
                max_i, max_j = i, j
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


# Example usage:
input_seq1 = "FPLVSG"
input_seq2 = "YPLASG"
input_gap_penalty = 8
aligned_seq1, aligned_seq2, alignment_score = local_alignment(input_seq1, input_seq2, input_gap_penalty)
print("Local Alignment:")
print("Sequence 1:", aligned_seq1)
print("Sequence 2:", aligned_seq2)
print("Score:", alignment_score)
