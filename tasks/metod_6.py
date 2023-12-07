from math import pi, cos, sin, sqrt, exp
import matplotlib.pyplot as plt
import sys


def user_data():
    function_trigonometry = input('Specify is it "cos" or "sin": ')
    if function_trigonometry == "cos":
        print("y' = x + cos(y / k)")
    else:
        print("y' = x + sin(y / k)")

    coefficient = eval(input('Specify the k (coefficient): '))
    print('Since y(x0) = y0, you have to specify')
    x_0 = float(input('x0: '))
    y_0 = float(input('y0: '))
    print('Now choose the interval [a, b]')
    a = float(input('a: '))
    b = float(input('b: '))
    return function_trigonometry, a, b, y_0, coefficient


def graphic(x_array, y_array, label):
    plt.plot(x_array, y_array, 'o-r')
    plt.title(label)
    plt.grid()
    plt.show()


def user_data_show(x_array, y_array):
    print('step(i)\t|', 'x\t\t|', 'y', )
    print('------------------------')
    for i in range(len(x_array)):
        print(" ", i, "\t|", round(x_array[i], 3), "\t|", round(y_array[i], 3))


def method_euler():
    print('\n--------------------Euler Method--------------------\n')
    function_trigonometry, a, b, y_0, coefficient = user_data()
    step = 0.1
    x_array = []
    while a <= b + step:
        x_array.append(a)
        a = a + step

    y_array = [y_0]
    for i in range(len(x_array) - 1):
        if function_trigonometry == 'sin':
            y_i = y_array[i] + step * (x_array[i] + sin(y_array[i] / coefficient))
        else:
            y_i = y_array[i] + step * (x_array[i] + cos(y_array[i] / coefficient))
        y_array.append(y_i)

    user_data_show(x_array, y_array)
    graphic(x_array, y_array, 'Euler Method')


def method_euler_cauchy():
    print('\n--------------------Euler-Cauchy Method--------------------\n')
    function_trigonometry, a, b, y_0, coefficient = user_data()
    step = 0.1
    x_array = []
    while a <= b + step:
        x_array.append(a)
        a = a + step

    y_array = [y_0]
    for i in range(len(x_array) - 1):
        if function_trigonometry == 'sin':
            y_i = y_array[i] + (step / 2) * (x_array[i] + sin(y_array[i] / coefficient) + x_array[i] + step + sin(
                (y_array[i] + step * (x_array[i] + sin(y_array[i] / coefficient))) / coefficient))
        else:
            y_i = y_array[i] + (step / 2) * (x_array[i] + cos(y_array[i] / coefficient) + x_array[i] + step + cos(
                (y_array[i] + step * (x_array[i] + cos(y_array[i] / coefficient))) / coefficient))
        y_array.append(y_i)

    user_data_show(x_array, y_array)
    graphic(x_array, y_array, 'Euler-Cauchy Method')


def user_method_choose():
    print('\n1 - Euler method\n2 - Euler-Cauchy method\n3 - Exit')
    choice = int(input('\n>>> '))
    if choice == 1:
        method_euler()
        user_method_choose()
    elif choice == 2:
        method_euler_cauchy()
        user_method_choose()
    elif choice == 3:
        sys.exit(0)
    else:
        print('You have chosen the wrong number!')


user_method_choose()
