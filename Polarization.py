# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
	Программа "Polarization".
	Предназначена для постройки графика Поляризации электромагнитных волн по выбору параметров (шкалы) пользователем.
	Программа позваляет определить поляризацию электромагнитной волны в для выражения: E_x0=1, E_y0=1, φ=π/2.
	Результатом работы данной программы является график поляризации электромагнитных волн, управляемый пользователем.
"""


import math as mt  # импорт библиотеки math
import matplotlib.pyplot as plt  # импорт библиотеки matplotlib
from matplotlib.widgets import Slider  # импорт библиотеки matplotlib.widgets

vkt = 60  # кол-во отображаемых векторов.
y_min = 0  # начало y (ограничение построения).
y_max = 4  # конец y (ограничение построения).

# Инициализация списков для координат x, y, z; а так же списков координат векторов Ex, Ey, Ez.
x, y, z, e_x, e_y, e_z = (list() for _ in range(6))

# Инициализируем и задаем Ex0, Ey0.
e_x0, e_z0 = 1, 1

# Инициализируем и задаем начальный момент времени.
time = 2

# Вызов из библиотеки math метод π; назначаем начальный угол.
pi = mt.pi / 2

# Вызов цикла for для прохождения к значению Np от нуля, с шагом i.
# i является частью внутренних данных из переменной Np.
for i in range(vkt):
	# Заапись переменных в список (x, y, z) координат.
	x.append(0)
	y.append(y_min + (y_max - y_min) / (vkt - 1) * (i - 1))
	z.append(0)

# Метод figure – внешний контейнер для графики matplotlib.
# Аргумента figsize позволяет установить размер графического облака (измеряется в дюймах).
fig = plt.figure(figsize=(11, 9))

# Метод gca используется для получения текущего экземпляра Axes на текущем рисунке.
# Аргумента projection используется для установки угла вида отображения 3D графика.
ax = fig.gca(projection='3d')

# Метод view_init используется для установки начальной высоты и азимутальных углов для положения камеры.
ax.view_init(10, 55)


# Функция для очистки списка векторов.
def AllClear():
	# Метод clear удаляет из списка все элементы.
	e_x.clear()
	e_y.clear()
	e_z.clear()
	ax.clear()


# Функция для отрисовки векторов.
def ShowAx(l):
	# Метод plot3D для "окантовка" векторов.
	ax.plot3D(e_x, y, e_z, 'r')

	# Метод set_xlim, set_ylim, set_zlim используется для установки диапазонов осей чтобы обрезать или расширить
	# представление до определенных пределов.
	ax.set_xlim(-1, 1)
	ax.set_ylim(y_min, y_max)
	ax.set_zlim(-1, 1)

	# Метод set_xlabel, set_ylabel, set_zlabel используется для установки надписей возле своих осей (способом '$x$') и
	# установка размеров надписи.
	ax.set_xlabel('$x$', fontsize=20)
	ax.set_ylabel('$y$', fontsize=20)
	ax.set_zlabel('$z$', fontsize=20)

	# Создаем наименование нашему графику.
	s = 'Поляризации электромагнитных волн при time = ' + str("%.2f" % l)

	# Добавлеяем надпись в графическое окно.
	ax.set_title(s, fontsize=20, color='#E066FF')


# Функция перерасчёта векторов при заданных значениях.
def refresh(val):
	# Передача времени.
	tm = s_pol_time.val

	# Передача угла π.
	Pi = s_pol_pi.val

	# Передача e_x0.
	Ex0 = s_pol_ex.val

	# передача e_y0.
	Ez0 = s_pol_ey.val

	# Функция для очистки списка векторов.
	AllClear()

	for content in range(vkt):
		# Запись координат вектора e_x по формуле.
		e_x.append(Ex0 * mt.cos(2 * mt.pi * y[content] - 2 * mt.pi * tm + Pi))

		# Запись координат вектора e_y по формуле.
		e_y.append(0)

		# Запись координат вектора e_z по формуле.
		e_z.append(Ez0 * mt.cos(2 * mt.pi * y[content] - 2 * mt.pi * tm))

	# Отображение всех векторов при изменении параметров.
	for indicator in range(vkt):

		ax.quiver(
			x[indicator],
			y[indicator],
			z[indicator],
			e_x[indicator],
			e_y[indicator],
			e_z[indicator],
			# Цвет линий в объекте.
			color='#32CD32',
			# Жирность линий в объекте.
			linewidth=2.0
		)

	# Функция для отрисовки векторов.
	ShowAx(tm)

	sett()

	# Создание и установка легенды.
	lgnd = ax.legend(['Оконтовка.', 'Вектор Поляризации.'], loc='upper center', shadow=False)
	lgnd.get_frame().set_facecolor('#ffb19a')


for i in range(vkt):
	# Запись координат вектора e_x по формуле.
	e_x.append(e_x0 * mt.cos(2 * mt.pi * y[i] - 2 * mt.pi * time + pi))

	# Запись координат вектора e_y по формуле.
	e_y.append(0)

	# Запись координат вектора e_z по формуле.
	e_z.append(e_z0 * mt.cos(2 * mt.pi * y[i] - 2 * mt.pi * time))


# Отображение всех векторов на начальном графике.
for i in range(vkt):
	# Основаная оработа графиков с параметрами.
	ax.quiver(
		x[i],
		y[i],
		z[i],
		e_x[i],
		e_y[i],
		e_z[i],
		# Цвет линий в объекте.
		color='#32CD32',
		# Жирность линий в объекте.
		linewidth=2.0
	)


# Функция отрисовки векторов.
ShowAx(time)

# Установка расположения графика.
fig.subplots_adjust(left=0.0, right=1.0, top=0.9, bottom=0.25)


# Настройка облака и легенды.
def sett():
	# Создание и установка легенды.
	lgnd = ax.legend(['Оконтовка.', 'Вектор Поляризации.'], loc='upper center', shadow=False)
	lgnd.get_frame().set_facecolor('#ffb19a')

	# Устонавливаем наименование заголовка.
	plt.gcf().canvas.set_window_title('Поляризации электромагнитных волн')


# Установка расположений слайдеров.
ax_pol_time = plt.axes([0.1, 0.03, 0.8, 0.04], facecolor='#B5B5B5')
ax_pol_pi = plt.axes([0.1, 0.07, 0.8, 0.04], facecolor='#EEAEEE')
ax_pol_ex = plt.axes([0.1, 0.11, 0.8, 0.04], facecolor='#CD919E')
ax_pol_ey = plt.axes([0.1, 0.15, 0.8, 0.04], facecolor='#CDBA96')

# Управление слайдерами.
s_pol_ey = (Slider(ax_pol_ey, r'$E_yo=$', 0, 1, valinit=e_z0, valfmt='%1.2f', color='#66CDAA'))
s_pol_ex = Slider(ax_pol_ex, r'$E_xo=$', 0, 1, valinit=e_x0, valfmt='%1.2f', color='#7FFFD4')
s_pol_pi = Slider(ax_pol_pi, 'φ=', -mt.pi, mt.pi, valinit=pi, valfmt='%1.2f', color='#20B2AA')
s_pol_time = Slider(ax_pol_time, 'time=', 0, 4, valinit=time, valfmt='%1.2f', color='#3CB371')

# Настраиваем фришт данным графы.
s_pol_ey.label.set_size(15)
s_pol_ex.label.set_size(15)
s_pol_pi.label.set_size(15)
s_pol_time.label.set_size(15)

# Вызов слайдеров.
s_pol_time.on_changed(refresh)
s_pol_pi.on_changed(refresh)
s_pol_ex.on_changed(refresh)
s_pol_ey.on_changed(refresh)

# Вызов фун-ии для настройка облака и легенды.
sett()

# Показывать объекты графика и фигуры.
plt.show()
