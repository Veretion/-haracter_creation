import win32api
import win32gui
from random import choice
from time import sleep, time

from Engine import grid_mass, mass, print_grid

dc = win32gui.GetDC(0)

x_int = 200
y_int = 200
long = 100

all_nums = 0
maas = 0

print(1)

file = open('mass3.txt', 'r').read().split('\n')
mass_all = [i.split(',') for i in file]

print(2)


def sortByLength(inputStr):
	return len(inputStr)


mass_all.sort()
mass_all.sort(key=sortByLength)
# mass_all = mass_all[::-1]
print(3)


for mrun in mass_all:
	print_grid(grid_mass)
	print(mrun)

	for ii in mrun:
		n = mass[int(ii)]
		for i in n[1]:
			win32gui.SetPixel(dc, i[0], i[1], win32api.RGB(255, 0, 0))

		sleep(0.01)
	sleep(1)







