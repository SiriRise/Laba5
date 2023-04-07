# Задана рекуррентная функция. Область определения функции – натуральные числа.
# Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
# Определить границы применимости рекурсивного и итерационного подхода.
# Результаты сравнительного исследования времени вычисления представить в табличной и графической форме.


import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(4000)
try:
    n = int(input('Введите натуральное число n: '))

    def f_rek(n):
        if n == 1 or n == 2:
            return 1
        else:
            return f_rek(n - 2) * (n - 1)

    def f_iter(n):
        f_n =[1]*(n+1)
        for i in range(3, n + 1):
            f_n[i] = f_n[i-2] * (i-1)
        return f_n[n]

    start = time.time()
    result = f_rek(n)
    end = time.time()
    print("\nрекурсия:", result, "\nВремя:", end - start)
    start = time.time()
    result = f_iter(n)
    end = time.time()
    print("\nитерация:", result, "\nВремя:", end - start)

    rek_times = []
    rek_values = []
    iter_times = []
    iter_values = []
    n_values = list(range(1, n + 1))

    for n in n_values:
        start = time.time()
        rek_values.append(f_rek(n))
        end = time.time()
        rek_times.append(end - start)

        start = time.time()
        iter_values.append(f_iter(n))
        end = time.time()
        iter_times.append(end - start)

    t_data = []
    for i, n in enumerate(n_values):
        t_data.append([n, rek_times[i],rek_values[i], iter_times[i], iter_values[i]])
    print('{:<5}{:<20}{:<20}{:<20}{:<20}'.format('n', 'Время рекурсии','Значение рекурсии', 'Время итерации','Значение итерации'))
    for data in t_data:
        print('{:<5}{:<20}{:<20}{:<20}{:<20}'.format(data[0], data[1], data[2], data[3], data[4]))

















except ValueError:
    print('Перезагрузите программу и введите натуральное число')

