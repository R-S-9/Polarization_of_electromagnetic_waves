# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
    Программа "Polarization_in_space".
    Код проекции вектора напряжённости магнитного поля на плоскость y=0.
    Вид в пространстве.
"""

import matplotlib.pyplot as plt  # импорт библиотеки matplotlib.
import numpy as np  # импорт библиотеки numpy.
import math as mt  # импорт библиотеки math.

vkt = 30  # кол-во узлов сетки.
y_min = 0  # начало y (ограничение построения).
y_max = 2  # конец y (ограничение построения).

# Инициализация списков для координат x, y, z; а так же списков координат векторов Ex, Ey, Ez.
x, y, z, e_x, e_y, e_z = (list() for _ in range(6))

# Инициализируем и задаем Ex0, Ey0 напряженности электрического поля.
e_x0, e_z0 = 1, 1

# Инициализируем и задаем начальный момент времени.
time = 2

# Вызов цикла for для прохождения к значению vkt от нуля, с шагом i.
# i является частью внутренних данных из переменной vkt.
for i in range(vkt):
	# Заапись переменных в список (x, y, z) координат.
	x.append(0)
	y.append(y_min + (y_max - y_min) / (vkt - 1) * (i - 1))
	z.append(0)

for i in range(0, vkt):
	# Запись координат вектора e_x по формуле.
	e_x.append(e_x0 * mt.cos(2 * mt.pi * y[i] - 2 * mt.pi * time + mt.pi / 2))

	# Запись координат вектора e_z по формуле.
	e_z.append(e_z0 * mt.cos(2 * mt.pi * y[i] - 2 * mt.pi * time))

theta = np.linspace(-np.pi, np.pi, 200)

# Основаная работа графиков с параметрами.
plt.plot(np.sin(theta), np.cos(theta), color='blue', linestyle='dashed', alpha=0.5)
plt.quiver(x, z, e_x, e_z, scale=1, width=0.01, units='xy', color='#32CD32')
plt.grid(True, which='major', color='black', linestyle='dashed', alpha=0.5)

# задали рабочую область по х и y.
plt.xlim(-1, 1)
plt.ylim(-1, 1)

# Метод xlabel и ylabel используется для установки надписей возле своих осей (способом '$x$') и
# установка размеров надписи.
plt.xlabel('$x$', fontsize=16)
plt.ylabel('$z$', fontsize=16)
plt.axis('equal')

# Устонавливаем наименование заголовка.
plt.gcf().canvas.set_window_title('Поляризация электромагнитных волн')

plt.show()
