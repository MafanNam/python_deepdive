import re
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import directed_hausdorff

FILES = ['1.txt', '2.txt', '3.txt', '4.txt']
TIME_X = []
DATA = []


def read_data(filename):
    with open(filename, 'r') as file:
        data_str = re.findall(r"[-+]?\d*\.\d+|\d+", file.read())
        return [float(i) for i in data_str]


def init_data():
    global TIME_X, DATA
    TIME_X = []
    DATA = [read_data(file) for file in FILES]
    for data in DATA:
        TIME_X.append([i / len(data) for i in range(len(data))])


def normalize_data():
    global DATA
    for m in range(len(DATA)):
        Z = DATA[m]
        Z_min = np.min(Z)
        Z_max = np.max(Z)
        z_norm = [(z - Z_min) / (Z_max - Z_min) for z in Z]
        DATA[m] = np.array(z_norm)

    for m in range(len(DATA)):
        ż = DATA[m]
        ż_min = np.min(ż[1:-1])
        ż_max = np.max(ż[1:-1])
        ż_norm = [(ż[k] - ż_min) / (ż_max - ż_min) for k in range(1, len(ż) - 1)]
        DATA[m][1:-1] = ż_norm


def get_derivative(data):
    derivative = np.zeros_like(data)
    for k in range(3, len(data) - 3):
        derivative[k] = (1 / 60) * (
                    data[k + 3] - 9 * data[k + 2] + 45 * data[k + 1] - 45 * data[k - 1] + 9 * data[k - 2] - data[k - 3])
    return derivative


def get_phaze_data():
    global DATA
    return [get_derivative(data) for data in DATA]


def get_matrix():
    dd = [[], [], [], []]
    for i in range(4):
        for j in range(4):
            d = directed_hausdorff(np.column_stack((TIME_X[i], DATA[i])), np.column_stack((TIME_X[j], DATA[j])))[0]
            dd[i].append(d)
    sums = [sum(row) for row in dd]
    return sums.index(min(sums))


def get_phase_plot():
    index = get_matrix()
    dominant_index = index
    fig, ax = plt.subplots()
    labels = ['ЕКГ 1', 'ЕКГ 2', 'ЕКГ 3', 'ЕКГ 4']
    colors = ['#FF5733', '#FFC300', '#DAF7A6', '#5DADE2']

    for i in range(4):
        linestyle = '-.' if i == dominant_index else '-'
        ax.plot(get_phaze_data()[i], DATA[i], label=labels[i] + (' є домінантною' if i == dominant_index else ''),
                color=colors[i], linewidth=1.5, linestyle=linestyle)

    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_title('Фазові Графіки')
    ax.legend(prop={'size': 8})
    ax.tick_params(axis='x', colors='gray')
    ax.tick_params(axis='y', colors='gray')
    fig.tight_layout()

init_data()
normalize_data()
get_phase_plot()
plt.show()