import numpy as np
from lb6_7_1 import blosum62


# Function to find the maximum matches given the threshold T
def find_max_matches(seq1, seq2, blosum62_matrix, gap_penalty, threshold_values):
    results = {}
    for threshold in threshold_values:
        H = np.zeros((len(seq1) + 1, len(seq2) + 1))  # Initialize the matrix
        for i in range(1, len(seq1) + 1):
            for j in range(1, len(seq2) + 1):
                match = H[i - 1][j - 1] + blosum62_matrix[seq1[i - 1]][seq2[j - 1]]
                delete = H[i - 1][j] + gap_penalty
                insert = H[i][j - 1] + gap_penalty
                H[i][j] = max(0, match, delete, insert)  # Fill the matrix
        H[H < threshold] = 0  # Apply thresholding
        matches = np.count_nonzero(H)  # Count the non-zero elements
        results[threshold] = matches
    return results


# Function to perform traceback and generate alignments
def traceback_alignment(H, seq1, seq2, blosum62_matrix, gap_penalty):
    i, j = np.unravel_index(np.argmax(H), H.shape)  # Find the maximum value's index
    align_seq1, align_seq2 = [], []
    while H[i][j] > 0:
        if H[i][j] == H[i - 1][j - 1] + blosum62_matrix[seq1[i - 1]][seq2[j - 1]]:
            align_seq1.append(seq1[i - 1])
            align_seq2.append(seq2[j - 1])
            i -= 1
            j -= 1
        elif H[i][j] == H[i - 1][j] + gap_penalty:
            align_seq1.append(seq1[i - 1])
            align_seq2.append('-')
            i -= 1
        else:
            align_seq1.append('-')
            align_seq2.append(seq2[j - 1])
            j -= 1
    align_seq1 = align_seq1[::-1]
    align_seq2 = align_seq2[::-1]
    return ''.join(align_seq1), ''.join(align_seq2)


def main():
    seq1 = "REPERE"
    seq2 = "REDIHDRE"
    gap_penalty = 8
    threshold = 20

    H = np.zeros((len(seq1) + 1, len(seq2) + 1))  # Initialize the matrix

    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            match = H[i - 1][j - 1] + blosum62[seq1[i - 1]][seq2[j - 1]]
            delete = H[i - 1][j] + gap_penalty
            insert = H[i][j - 1] + gap_penalty
            H[i][j] = max(0, match, delete, insert)  # Fill the matrix

    H[H < threshold] = 0  # Apply thresholding

    threshold_values = range(0, 50, 5)
    results = find_max_matches(seq1, seq2, blosum62, gap_penalty, threshold_values)

    for threshold, matches in results.items():
        print(f"T={threshold}: {matches} matches")

    H = np.zeros((len(seq1) + 1, len(seq2) + 1))
    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            match = H[i - 1][j - 1] + blosum62[seq1[i - 1]][seq2[j - 1]]
            delete = H[i - 1][j] + gap_penalty
            insert = H[i][j - 1] + gap_penalty
            H[i][j] = max(0, match, delete, insert)
    H[H < threshold] = 0

    align_seq1, align_seq2 = traceback_alignment(H, seq1, seq2, blosum62, gap_penalty)
    print(f"Alignment:\n{align_seq1}\n{align_seq2}")


if __name__ == "__main__":
    main()
