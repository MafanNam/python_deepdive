from scipy.interpolate import make_interp_spline

import matplotlib.pyplot as plt
import numpy as np

import random
import math

M = int(input("Enter the number of experiments(M) : "))
N = int(input("Enter the number of alternatives in each experiment(N) : "))

min_val = int(input("Random Mim: "))
max_val = int(input("Random Max: "))

delta_input = int(input("Start delta: "))

experiments, results = [[random.randint(min_val, max_val) for _ in range(N)] for _ in range(M)], []

t = round(N / math.e)

results_check = []


# Monte Carlo Method
def Monte_carlo_Method(delta_input, t):
    results = []
    for j in range(M):
        opt_max, all_max = max([experiments[j][k] for k in range(t)]), max(experiments[j])

        first_max, delta = 0, (delta_input / 100) * all_max

        for i in range(t, N):
            if opt_max <= experiments[j][i]:
                first_max = experiments[j][i]
                if abs(first_max - all_max) <= delta:
                    results.append(1)
                    results_check.append(1)
                    break
                else:
                    results.append(0)
                    results_check.append(0)
                    break

    P = (sum(results) / M)
    return P


# Виведення масиву чисел (з поступкою 0%)
res_1 = Monte_carlo_Method(0, 37)
print(f'{res_1}, {results_check}')

P_delta_zero = Monte_carlo_Method(delta_input, t)
print(f"Probability(P(∆)) ∆ = 0: {int(P_delta_zero * 100)}%")

deltas, different_t = [0, 2, 4, 6, 8, 10], [i * 10 - 5 for i in range(1, 11)]
results_dict = {}

for delta in deltas:
    results_dict[delta] = []
    for t in different_t:
        res = Monte_carlo_Method(delta, t)
        results_dict[delta].append(res)

j = 0
for i in results_dict:
    x_values = different_t
    y_values = results_dict[i]

    plt.figure(figsize=(12, 6))
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('t')
    plt.ylabel('P')
    plt.title(f'Concession = {j}')

    plt.xticks(range(min(x_values), max(x_values) + 1, 5))
    j += 2
    plt.grid(True)
    plt.show()

results_p, t = [], round(N / math.e)
for delta in deltas:
    res1 = Monte_carlo_Method(delta, t)
    results_p.append(res1)
print(results_p)

baseline = results_p[0]

# Обчислення відсоткової різниці між значеннями
for value in results_p[1:]:
    percentage_difference = ((value - baseline) / baseline) * 100
    print(f" % difference between {baseline} and {value}: {percentage_difference:.2f}%")

x = deltas
y, res_data = results_p, results_p
xnew = np.linspace(min(x), max(x), 1000)
spl = make_interp_spline(x, y, k=2)
y_smooth = spl(xnew)
plt.plot(xnew, y_smooth, label='∆ = 0')
plt.plot(deltas, res_data, marker='o')
plt.title('Залежність максимальної ймовірності успіху від велечини поступки')
plt.xlabel("Поступка")
plt.ylabel("Ймовірність")
plt.grid(True)
plt.ylim(0, 0.70)
plt.show()

deltas, result_t = [0, 2, 4, 6, 8, 10], []
for delta in deltas:
    max_el = max(results_dict[delta])
    t = (results_dict[delta].index(max_el) + 1) * 10 - 5
    result_t.append(t)
x = deltas
y, res_data = result_t, result_t
xnew = np.linspace(min(x), max(x), 700)
spl = make_interp_spline(x, y, k=2)
y_smooth = spl(xnew)
plt.plot(xnew, y_smooth, label='∆ = 0')
plt.plot(deltas, res_data, marker='o')
plt.title('Залежність номеру зупинки від велечини поступки')
plt.xlabel("Поступка")
plt.ylabel("Крок зупинки (t*)")
plt.grid(True)
plt.ylim(0, 35)
plt.show()

print(result_t)

baseline_2 = result_t[0]

# Обчислення відсоткової різниці між значеннями
for value in result_t[1:]:
    percentage_difference = ((value - baseline_2) / baseline_2) * 100
    print(f" % difference between {baseline_2} and {value}: {percentage_difference:.2f}%")
