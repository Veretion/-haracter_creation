
import win32con
import win32api
import win32gui
import sys
from time import sleep, time
from PIL import Image, ImageDraw
from random import randint, random, choice, choices, sample, shuffle
import mouse

dc = win32gui.GetDC(0)


def led_horiz(x_int, y_int, width, long):  # --
	x_int -= 1
	y_int -= 2
	mass = []

	# tran = 7

	if width % 2 == 0:
		z = round(width/2)
	else:
		z = round((width-1)/2)

	for y in range(z):  # верхняя часть
		for x in range(-2, long+1):
			if x < z-y-2:
				continue
			elif x > long+y-z:
				continue
			else:
				mass.append([x + x_int, y_int+y])

	if width % 2 != 0:
		for i in range(-2, long+1):
			mass.append([i + x_int, round(y_int+(((width-1)/2)+1))-1])

	for y in range(width-z, width):  # нижняя часть
		for x in range(-2, long + 1):
			if x < -2-(2*z) + z+y:
				continue
			elif x > long-y+z:
				continue
			else:
				mass.append([x + x_int, y_int + y])
	return mass


def led_vertic(x_int, y_int, width, long):  # --
	x_int -= 2
	y_int -= 1
	mass = []

	# tran = 7

	if width % 2 == 0:
		z = round(width/2)
	else:
		z = round((width-1)/2)

	for x in range(z):  # левая часть
		for y in range(-2, long+1):
			if y < z-x-2:
				continue
			elif y > long+x-z:
				continue
			else:
				mass.append([x + x_int, y_int+y, win32api.RGB(255, 0, 0)])

	if width % 2 != 0:
		for i in range(-2, long+1):
			mass.append([round(x_int+(((width-1)/2)+1))-1, i+y_int, win32api.RGB(255, 0, 0)])

	for x in range(width-z, width):  # правая часть
		for y in range(-2, long + 1):
			if y < -2-(2*z) + z+x:
				continue
			elif y > long-x+z:
				continue
			else:
				mass.append([x + x_int, y_int + y])
	return mass


def led_dig1(x_int, y_int, width, long):
	x_int -= 2
	y_int -= 2
	mass = []

	z = width/2 if width % 2 == 0 else (width-1)/2
	z = round(z)
	for x in range(long):
		for y in range(-z, width-z):
			if y_int + x+y < y_int or y + y_int + x > y_int+long:
				continue
			mass.append([x + x_int, y_int + y + x])
	return mass


def led_dig2(x_int, y_int, width, long):
	x_int += 0
	y_int += 0
	mass = []

	z = width/2 if width % 2 == 0 else (width-1)/2
	z = round(z)
	for x in range(0, -long, -1):
		for y in range(-z, width-z):
			if y_int + -x+y < y_int or y + y_int + -x > y_int+long:
				continue
			mass.append([x + x_int, y_int + y + -x])
	return mass


def grid():
	l_id = 0
	xx = 0
	yy = 0
	mass = []

	for i in range(3):
		for ii in range(3):
			mass.append([str(l_id), led_horiz(x_int+xx, y_int+yy, 5, long), 'horiz', [x_int+xx, y_int+yy], [x_int+long+xx, y_int+yy]])
			mass.append([str(l_id+1), led_vertic(x_int+xx, y_int+yy, 5, long), 'vertic', [x_int+xx, y_int+yy], [x_int+xx, y_int+long+yy]])
			mass.append([str(l_id+2), led_dig1(x_int+xx, y_int+yy, 7, long), 'dig1', [x_int+xx, y_int+yy], [x_int+long+xx, y_int+long+yy]])
			mass.append([str(l_id+3), led_dig2(x_int+long+xx, y_int+yy, 7, long), 'dig2', [x_int+long+xx, y_int+yy], [x_int+xx, y_int+long+yy]])

			l_id += 4
			yy += long
		xx += long
		yy = 0

	xx = long*3
	for i in range(3):
		mass.append([str(l_id), led_vertic(x_int+xx, y_int+yy, 5, long), 'vertic', [x_int+xx, y_int+yy], [x_int+xx, y_int+long+yy]])
		yy += long
		l_id += 1

	xx = 0
	yy = long*3
	for i in range(3):
		mass.append([str(l_id), led_horiz(x_int+xx, y_int+yy, 5, long), 'horiz', [x_int+xx, y_int+yy], [x_int+long+xx, y_int+yy]])
		xx += long
		l_id += 1
	return mass


def create_grid():
	grid_mass = []

	for i in mass:
		for ii in i[1]:
			if [ii[0], ii[1]] in grid_mass:
				continue
			grid_mass.append([ii[0], ii[1]])
	return grid_mass


def print_grid(grid_mass):
	for i in grid_mass:
		win32gui.SetPixel(dc, i[0], i[1], win32api.RGB(64, 0, 0))


# создание массива
x_int = 100
y_int = 100
long = 7#100
mass = grid()
grid_mass = create_grid()


def main():
	mass_all = []
	all_nums = 0
	maas = 0

	while True:
		ps = [x_int, y_int+long]
		mrun = []
		warn = False
		while ps != [x_int+long*3, y_int+long]:
			cm = []  # choice_mass
			zet = True
			for i in mass:
				if i[3] == ps or i[4] == ps:
					if i in mrun:
						continue
					zet = True
					cm.append(i)
			if not zet:
				continue
			zet = False
			if cm:
				im = choice(cm)
			else:
				warn = True
				break

			ps = im[3] if ps != im[3] else im[4]
			mrun.append(im)

		#
		if warn:
			continue

		als = []
		for i in mrun:
			als.append(i[0])
		als = ','.join(als)
		# print(als)
		# print_grid(grid_mass)
		# for ii in mrun:
		# 	for i in ii[1]:
		# 		win32gui.SetPixel(dc, i[0], i[1], win32api.RGB(255, 0, 0))
		# 	sleep(0.06)
		# sleep(2)

		if als not in mass_all:
			mass_all.append(als)
			all_nums += 1
		if all_nums % 10000 == 0 and maas < all_nums/10000:
			file = open('mass4.txt', 'w')
			file.write('\n'.join(mass_all))
			file.close()
			maas += 1
			print(all_nums, maas)
# main()



