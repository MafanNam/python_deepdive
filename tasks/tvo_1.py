import openpyxl, math
from matplotlib import pyplot as plt

wb = openpyxl.load_workbook('DATA.xlsx')
ws = wb.active

names = [ws[1][i].value for i in range(0, 11)]
values = [[], [], [], [], [], [], [], [], [], [], []]
sum_column = [[], [], [], [], [], [], [], [], [], [], []]

for row in range(2, 2002):
    for column in range(11):
        values[column].append(float(ws[row][column].value))

# Середнє арифметичне стовбця
average = list(map(lambda x: sum(x) / 2000, values))

for i in range(len(values[0])):
    for j in range(11):
        sum_column[j].append((values[j][i] - average[j]) ** 2)

# по формуле різниці квадратів
for suma in range(len(sum_column)):
    sum_column[suma] = math.sqrt(sum(sum_column[suma]) / (len(sum_column[suma]) - 1))

fig = plt.figure(figsize=(10, 7))
plt.bar(names, sum_column)

plt.show()