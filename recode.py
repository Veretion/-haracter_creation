import win32con
import win32api
import win32gui
import sys
from time import sleep, time
from PIL import Image, ImageDraw
from random import randint, random, choice, choices, sample, shuffle
import mouse

from Engine import mass


dc = win32gui.GetDC(0)
file = open("lemma.txt", 'r').read()
# filem = open('mass3.txt', 'r').read().split('\n')[:1200]
filem = open('mass3.txt', 'r').read().split('\n')[::-1]
# filem = filem[:1600]


def holine(x, y):
	for i in range(7):
		win32gui.SetPixel(dc, i+x, y, win32api.RGB(0, 0, 0))


def veline(x, y):
	for i in range(7):
		win32gui.SetPixel(dc, x, i+y, win32api.RGB(0, 0, 0))


def diline1(x, y):
	for i in range(7):
		win32gui.SetPixel(dc, x+i, i+y, win32api.RGB(0, 0, 0))


def diline2(x, y):
	for i in range(7):
		win32gui.SetPixel(dc, x+7-i-7, i+y, win32api.RGB(0, 0, 0))


filem = [i.split(',') for i in filem]


def sortByLength(inputStr):
	return len(inputStr)


filem.sort()
filem.sort(key=sortByLength)
filem = filem[::-1][:2400]

xx = 0
yy = 0
mi = 0
for _ in range(35):  # y
	for _ in range(52):  # x
		ii = filem[mi]
		mi += 1

		for i in ii:
			z = mass[int(i)]
			x, y = z[3][0]-95, z[3][1]-55
			print(x, y)
			if z[2] == 'horiz':
				holine(x+xx, y+yy)
			if z[2] == 'vertic':
				veline(x+xx, y+yy)
			if z[2] == 'dig1':
				diline1(x+xx, y+yy)
			if z[2] == 'dig2':
				diline2(x+xx, y+yy)
		sleep(0.001)
		xx += 24
	yy += 25
	xx = 0














































