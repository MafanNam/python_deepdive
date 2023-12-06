import random


def find_max_path(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    ind = [[0] * cols for _ in range(rows)]
    path = [[""] * cols for _ in range(rows)]

    # print(ind)

    ind[0][0] = matrix[rows - 1][0]
    # print(ind)
    path[0][0] = f"{rows - 1},0"
    for i in range(1, rows):
        ind[i][0] = ind[i - 1][0] + matrix[rows - 1 - i][0]
        path[i][0] = path[i - 1][0] + f" -> {rows - 1 - i},0"
    for j in range(1, cols):
        ind[0][j] = ind[0][j - 1] + matrix[rows - 1][j]
        path[0][j] = path[0][j - 1] + f" -> {rows - 1},{j}"

    for i in range(1, rows):
        for j in range(1, cols):
            if ind[i - 1][j] > ind[i][j - 1]:
                ind[i][j] = matrix[rows - 1 - i][j] + ind[i - 1][j]
                path[i][j] = path[i - 1][j] + f" -> {rows - 1 - i},{j}"
            else:
                ind[i][j] = matrix[rows - 1 - i][j] + ind[i][j - 1]
                path[i][j] = path[i][j - 1] + f" -> {rows - 1 - i},{j}"

    return ind[rows - 1][cols - 1], path[rows - 1][cols - 1]


rows = 5
cols = 5

matrix = [[random.randint(-20, 20)
           for _ in range(cols)]
          for _ in range(rows)]

print('Unmarked Matrix:')
for row in matrix:
    for cell in row:
        print(f"{cell:3}", end=" ")
    print()

max_path_sum, max_path = find_max_path(matrix)
# print(max_path_sum)
# print(max_path)
print('\n' + '-'*40)
print('\nMarked Matrix:')

marked_matrix = [[str(matrix[i][j])
                  if f"{i},{j}" not in max_path
                  else f"({matrix[i][j]})"
                  for j in range(cols)]
                 for i in range(rows)]

for row in marked_matrix:
    for cell in row:
        print(f"{cell:5}", end=" ")
    print()

print("\nSum:", max_path_sum)
