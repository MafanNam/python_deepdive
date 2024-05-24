import numpy as np
from blosum62 import blosum62  # Assuming blosum62 is a module providing the BLOSUM62 matrix


def calculate_H_matrix(x, y, blosum62, gap_penalty):
    # Initialize the matrix H with zeros
    H = np.zeros((len(x) + 1, len(y) + 1))

    # Fill in the matrix H using dynamic programming
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            # Calculate the score for a match
            match = H[i - 1][j - 1] + blosum62[x[i - 1]][y[j - 1]]
            # Calculate the score for a deletion
            delete = H[i - 1][j] + gap_penalty
            # Calculate the score for an insertion
            insert = H[i][j - 1] + gap_penalty
            # Update H[i][j] with the maximum score among match, delete, insert, or 0
            H[i][j] = max(0, match, delete, insert)
    return H


def find_max_matches(x, y, blosum62, gap_penalty, T_values):
    results = {}
    for T in T_values:
        # Calculate the matrix H for given x, y, and parameters
        H = calculate_H_matrix(x, y, blosum62, gap_penalty)
        # Thresholding: set values below threshold T to 0
        H[H < T] = 0
        # Count the number of non-zero elements in H, which represents matches
        matches = np.count_nonzero(H)
        # Store the matches for this threshold T
        results[T] = matches
    return results


def traceback(H, x, y, blosum62, gap_penalty):
    # Find the indices of the maximum value in H
    i, j = np.unravel_index(np.argmax(H), H.shape)
    align_x, align_y = [], []
    # Traceback from the maximum value until reaching a cell with score 0
    while H[i][j] > 0:
        if H[i][j] == H[i - 1][j - 1] + blosum62[x[i - 1]][y[j - 1]]:
            align_x.append(x[i - 1])
            align_y.append(y[j - 1])
            i -= 1
            j -= 1
        elif H[i][j] == H[i - 1][j] + gap_penalty:
            align_x.append(x[i - 1])
            align_y.append('-')
            i -= 1
        else:
            align_x.append('-')
            align_y.append(y[j - 1])
            j -= 1
    # Reverse the alignments to get the correct order
    align_x = align_x[::-1]
    align_y = align_y[::-1]
    return ''.join(align_x), ''.join(align_y)


x = "AINDSQ"
y = "INTNINPD"
gap_penalty = 8
T = 20

# Calculate the matrix H for given x, y, and parameters
H = calculate_H_matrix(x, y, blosum62, gap_penalty)

# Thresholding: set values below threshold T to 0
H[H < T] = 0

print("Our matrix:")
print(H)
print("--" * 30)

# Define a range of threshold values to test
T_values = range(0, 50, 5)
# Find the number of matches for each threshold value
results = find_max_matches(x, y, blosum62, gap_penalty, T_values)

# Print the results for different threshold values
for T, matches in results.items():
    print(f"T={T}: {matches} matches", end='\n\n')

print("--" * 30)

# Recalculate the matrix H without thresholding for traceback
H = calculate_H_matrix(x, y, blosum62, gap_penalty)
# Perform traceback to find the optimal alignment
align_x, align_y = traceback(H, x, y, blosum62, gap_penalty)
print(f"Alignment:\n{align_x}\n{align_y}")
