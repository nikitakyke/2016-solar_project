import matplotlib.pyplot as plt

def graph_Vt():
    t = []  # массив с временем
    V = []  # массив с полной скоростью
    i = 0   #параметр, c использованием которого пропускается первая строка
    #Заполнение массива данными из файла stats.txt для графика V(t)
    with open('stats.txt') as stats_file:
        for line in stats_file:
            if i == 1:
                vx = float(line.split()[3])
                vy = float(line.split()[4])
                v = (vx ** 2 + vy ** 2) ** 0.5
                V.append(v)
                t.append(float(line.split()[0]))
            i = 1
    #график
    plt.scatter(t, V, s=10, c='red', marker='^')

    #Заголовок графика
    plt.title('Зависимость модуля скорости планеты от времени')

    #Заголовки осей
    plt.ylabel('Модуль скорости планеты, м/с')
    plt.xlabel('Время, с')

    #Показать график
    plt.show()

def graph_rt():
    t = []  # массив с временем
    r = []  # массив с расстоянием
    i = 0  # параметр, c использованием которого пропускается первая строка
    # Заполнение массива данными из файла stats.txt для построения графика r(t)
    with open('stats.txt') as stats_file:
        for line in stats_file:
            if i == 1:
                x = float(line.split()[1])
                y = float(line.split()[2])
                R = (x ** 2 + y ** 2) ** 0.5
                r.append(R)
                t.append(float(line.split()[0]))
            i = 1
    #график
    plt.scatter(t, r, s=10, c='blue', marker='^')

    #Заголовок графика
    plt.title('Зависимость расстояния спутника до звезды от времени')

    #Заголовки осей
    plt.ylabel('Расстояние спутника до звезды, м')
    plt.xlabel('Время, с')

    #Показать график
    plt.show()

def graph_Vr():
    r = []  # массив с расстоянием
    V = []  # массив с полной скоростью
    i = 0  # параметр, c использованием которого пропускается первая строка
    # Заполнение массива данными из файла stats.txt для построения графика V(r)
    with open('stats.txt') as stats_file:
        for line in stats_file:
            if i == 1:
                vx = float(line.split()[3])
                vy = float(line.split()[4])
                v = (vx ** 2 + vy ** 2) ** 0.5
                V.append(v)
                x = float(line.split()[1])
                y = float(line.split()[2])
                R = (x ** 2 + y ** 2) ** 0.5
                r.append(R)
            i = 1
    # график
    plt.scatter(r, V, s=10, c='green', marker='^')

    #Заголовок графика
    plt.title('Зависимость модуля скорости от расстояния до звезды')

    #Заголовки осей
    plt.xlabel('Расстояние спутника до звезды, м')
    plt.ylabel('Модуль скорости планеты, м/с')

    #Показать график
    plt.show()
