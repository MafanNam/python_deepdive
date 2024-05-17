from collections import Counter
import statistics
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from prettytable import PrettyTable
from tkinter import *

# Load data
rhythm1 = []
with open('Ритм.txt') as f:
    for line in f:
        rhythm1.append(float(line))

# Time series generation
i = 0
tt = 0
t = []
while i < len(rhythm1):
    t.append(tt)
    tt += 1
    i += 1

# x and y for scatter plot
i = min(rhythm1) - 50
x = []
y = []
while i < max(rhythm1):
    x.append(i)
    y.append(i)
    i += 1

# Calculations
attr12 = sum(rhythm1) / len(rhythm1)
attr11 = 60000 / attr12
attr13 = statistics.stdev(rhythm1)
b = Counter(rhythm1)
attr14 = b.most_common(1)
attr15_1 = attr14[0][1] / len(rhythm1)
attr15 = attr14[0][1] / len(rhythm1) * 100
attr16 = max(rhythm1) - min(rhythm1)
a1 = attr15_1 / 60000
a2 = attr14[0][0] / 60000
a3 = attr16 / 60000
attr17 = a1 / (2 * a2 * a3)
attr24 = b.most_common(1)
a2 = attr24[0][0] / 60000
attr27 = a1 / (2 * a2 * a3)

# Create the main window
win0 = Tk()
win0.title("Ритмограмма")
win0.geometry('1100x400')
win0.wm_geometry("+10+10")
win0.resizable(width=False, height=False)
win0.configure(bg='#2e2e2e')  # Dark background

# Configure matplotlib for dark mode
plt.style.use('dark_background')

# Rhythmogram plot
f1 = plt.figure(1, figsize=(16, 9))
ax_1 = plt.subplot(2, 1, 1)
ax_1.set_facecolor('#2e2e2e')
plt.title('Ритмограмма', color='white')
plt.ylabel('RRi, мс', color='white')
plt.plot(t, rhythm1, '#097770')
plt.grid(color='white', linestyle='--', linewidth=0.5)
canvas = FigureCanvasTkAgg(f1, win0)
canvas.get_tk_widget().place(x=1, y=1, width=1098, height=698)

# Statistical Table
Column = ['Показник', 'Ритмограма']
Pokaz = ['ЧСС, уд/хв', 'NN, мс', 'SDNN, мс', 'Mo, мс', 'AMo, %', 'MxDMn, мс', 'ІН']
atr1 = [attr11, attr12, attr13, attr14, attr15, attr16, attr17]

# Create the scattergram window
win1 = Toplevel(win0)
win1.title("Скаттерограма")
f2 = plt.figure(2, figsize=(11, 5))
win1.geometry('550x450')
win1.wm_geometry("+960+30")
win1.resizable(width=False, height=False)
ax1 = plt.subplot(1, 2, 1)
ax1.set_facecolor('#2e2e2e')
plt.title('Скаттерограма', color='white')
plt.xlabel('RRi+1, мс', color='white')
plt.ylabel('RRi, мс', color='white')
plt.scatter(rhythm1[1:len(rhythm1)], rhythm1[0:len(rhythm1) - 1], color='#b9925e', marker='.', edgecolors='black',
            s=100, linewidths=0.5)
plt.plot(x, y, 'k--', color='white')
canvas2 = FigureCanvasTkAgg(f2, win1)
canvas2.get_tk_widget().place(x=1, y=1, width=999, height=449)

# Create the histogram window
win2 = Toplevel(win1)
win2.title("Гістограма")
f3 = plt.figure(3, figsize=(16, 9))
win2.geometry('550x450')
win2.wm_geometry("+800+520")
win2.resizable(width=False, height=False)
ax1_1 = plt.subplot(1, 2, 1)
ax1_1.set_facecolor('#2e2e2e')
plt.title('Гістограма', color='white')
plt.xlabel('RRi, мс', color='white')
plt.ylabel('Кількість RR', color='white')
plt.hist(rhythm1, alpha=1, color='#b9925e', edgecolor='black')
canvas2 = FigureCanvasTkAgg(f3, win2)
canvas2.get_tk_widget().place(x=1, y=1, width=999, height=449)

# Statistical Table in console
table1 = PrettyTable(Column)
for i in range(len(Pokaz)):
    table1.add_row([Pokaz[i], float("{0:.5f}".format(atr1[i])) if i != 3 else atr1[i]])
print(table1)

win0.mainloop()
