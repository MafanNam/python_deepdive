# import openpyxl, math
# from matplotlib import pyplot as plt
#
# # Завантаження Excel-файлу та вибір активного аркуша
# wb = openpyxl.load_workbook('DATA.xlsx')
# ws = wb.active
#
# # Список назв показників (з першого рядка таблиці)
# names = [ws[1][i].value for i in range(0, 11)]
#
# values = [[], [], [], [], [], [], [], [], [], [], []]
#
# # Список квадратів відхилень від середнього
# sum_column = [[], [], [], [], [], [], [], [], [], [], []]
#
# for row in range(2, 2002):
#     for column in range(11):
#         values[column].append(float(ws[row][column].value))
#
# # Обчислення середніх значень показників
# average = list(map(lambda x: sum(x) / 2000, values))
#
# # Обчислення квадратів відхилень від середнього значення
# for i in range(len(values[0])):
#     for j in range(11):
#         sum_column[j].append((values[j][i] - average[j]) ** 2)
#
# # Обчислення стандартних відхилень
# for suma in range(len(sum_column)):
#     sum_column[suma] = math.sqrt(sum(sum_column[suma]) / (len(sum_column[suma]) - 1))
#
# for name, sum in list(zip(names, sum_column)):
#     print(name, round(sum * 100, 2))
#
# print("Найменше відхилення від середнього значення: Прод R " + str(min(sum_column)))
#
# fig = plt.figure(figsize=(10, 7))
# plt.bar(names, sum_column)
# plt.title("Відхилення від середнього значення")
# plt.xlabel("Показник")
# plt.ylabel("Значення")
# plt.show()




def generate_difference_table(x_values, y_values):
    n = len(x_values)
    difference_table = [[0] * n for _ in range(n)]

    for i in range(n):
        difference_table[i][0] = y_values[i]

    for j in range(1, n):
        for i in range(n - j):
            difference_table[i][j] = difference_table[i + 1][j - 1] - difference_table[i][j - 1]

    return difference_table

h = 0.5

def calculate_derivative_1():
    q = 0.76
    derivative_1 = (1 / h) * (-0.42+( (2 * q - 1) / 2) * (0.01) +( (3 * q ** 2 - 6 * q + 2) / 6) * 0.06 + ((
            2 * q ** 3 - 9 * q ** 2 + 11 * q - 3) / 12) * 0.015)
    return derivative_1

def calculate_second_derivative_1():
    q = 0.76
    second_derivative_1 = (1 / (h**2)) * (0.01 + (q - 1) * 0.06 + ((6 * (q ** 2) - 18 * q + 11) / 12) * 0.0015)
    return second_derivative_1

def calculate_derivative_2():
    q = 0.76
    derivative_2 = (1 / h) * (-0.195 +((2 * q - 1) / 2) * (0.235) +( (3 * q ** 2 - 6 * q + 2) / 6) * 0.105 + ((
            2 * q ** 3 - 9 * q ** 2 + 11 * q - 3) / 12) * (0.014))
    return derivative_2

def calculate_second_derivative_2():
    q = 0.76
    second_derivative_2 = (1 / (h ** 2)) * (0.235 + (q - 1) * 0.105 + ((6 * (q ** 2) - 18 * q + 11) / 12) * (0.014))
    return second_derivative_2

derivative_1 = calculate_derivative_1()
print(f"Похідна в точці 2.88 = {derivative_1:.3f}")

second_derivative_1 = calculate_second_derivative_1()
print(f"Друга похідна в точці 2.88 = {second_derivative_1:.3f}")

derivative_2 = calculate_derivative_2()
print(f"Похідна в точці 4.38 = {derivative_2:.3f}")

second_derivative_2 = calculate_second_derivative_2()
print(f"Друга похідна в точці 4.38 = {second_derivative_2:.3f}")