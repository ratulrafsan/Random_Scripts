import os, random, sys, time
from termcolor import colored

rows, columns = os.popen('stty size', 'r').read().split()
print(rows, columns)

chars  = ['0', '1', ' ']
colors = ['green','red','yellow','blue'] 

try:
	while True:
		row = ''
		i = 0
		for i in range(int(columns)):
			color = random.choice(colors)
			row = row + colored(random.choice(chars), color)
		print row
		time.sleep(.1)

	for c in ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']:
		s = ''
		for h in ['on_grey', 'on_red', 'on_green', 'on_yellow', 'on_blue', 'on_magenta', 'on_cyan', 'on_white']:
			s = s + colored('Hello world', c, h)
		print s
except (KeyboardInterrupt, SystemExit):
	sys.exit('Bye!')
