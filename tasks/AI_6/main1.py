import matplotlib.pyplot as plt
from scipy import signal
import numpy as np


def show_graphics(ecg1, t1, TAU):
    new_ecg1 = ecg1[0:len(ecg1) - TAU]
    new_ecg2 = ecg1[TAU:len(ecg1)]
    new_ecg5 = np.gradient(ecg1, t1)


    plt.figure(1, figsize=(16, 2))
    plt.plot(t1, ecg1, 'r'), plt.grid
    plt.xlabel('t')
    plt.ylabel('z(t)')
    plt.title('ECG №1')
    plt.figure(2, figsize=(16, 2))
    plt.plot(new_ecg1, new_ecg2, 'r'), plt.grid
    plt.xlabel('z(t-TAU)')
    plt.ylabel('z(t)')
    plt.title('FP №1')
    plt.figure(3, figsize=(16, 2))
    plt.xlabel('dz/dt')
    plt.ylabel('z(t)')
    plt.plot(new_ecg5, ecg1, 'r'), plt.grid
    plt.title('FP №2')


    plt.show()


ecg1 = []
with open('ECG.txt') as f:
    for line in f:
        inner_list = [elt.strip() for elt in line.split(' ')]

        for a in inner_list:
            if a!='':
                ecg1.append(float(a))


ecg2 = []
with open('ECG.txt') as f:
    for line in f:
        inner_list = [elt.strip() for elt in line.split(' ')]

        for a in inner_list:
            if a != '':
                ecg2.append(float(a))

f.close()
i = 0
tt = 0.01
t1 = []
while i < len(ecg1):
    t1.append(tt)
    tt += 0.05
    i += 1

i = 0
tt = 0.01
t2 = []
while i < len(ecg2):
    t2.append(tt)
    tt += 0.05
    i += 1

a = 1
while (a < 1) or (a > 2):
    a = int(input('1 or 2: '))

TAU = int(input('tau = '))
while (TAU < 1):
    TAU = int(input('should be greater than 1: '))

show_graphics(ecg1, t1, TAU)

