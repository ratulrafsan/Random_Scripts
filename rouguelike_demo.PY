#@author : Rafsan Ratul (ratulrafsan@gmail.com)
#An attempt to make a simple rouguelike game in python without using any external library
import os
import random
import platform
try:
    from msvcrt import getch #For windows
except ImportError: #For linux and maybe mac...
    def getch():
    
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def pressedkey():
    return getch()

          # 0   1   2   3   4   5   6   7   8   9  10   11  12  13  14  15
room = {1:['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'], # ^
	    2:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'], # |
	    3:['#','.','.','.','.','.','.','.','.','#','#','#','#','.','.','#'], # |
	    4:['#','.','.','.','.','.','.','#','.','#','.','.','.','.','.','#'], # |
	    5:['#','.','.','.','.','.','@','#','.','#','.','.','#','.','.','#'], # |
	    6:['#','.','.','.','.','.','.','#','.','.','.','.','#','.','.','#'], # x
	    7:['#','.','.','.','.','#','#','#','.','#','#','.','#','.','.','#'], # |
	    8:['#','.','.','.','.','.','.','.','.','.','#','#','#','.','.','#'], # |
	    9:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'], # |
	   10:['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']} # |
	    # <------------------------------y--------------------------------->

stuff  = {'wall'  :  "#",
          'player':  "@",
          'empty' :  ".",
          'money' :  "$",
          'chest' :  "C"}
#potion = ['hp','xp','dmg']
#weapon = ['sword','nuclear bomb','TNT']

	

pos = [] # 0 is X,1 is Y


def gamemap():
    for i in range(1,len(room)+1):
	    print "".join(room[i])

def player_pos():
    for i in range(1,len(room)+1):
		if stuff['player'] in room[i]:
			x_axis = i
			y_axis = room[i].index(stuff['player'])
			global pos
			del pos[:]
			pos.append(x_axis)
			pos.append(y_axis)

def updater():
	if platform.system() =='Windows':
		os.system('cls')
	elif platform.system() == 'Linux':
		os.system('clear') #For linux.. I don't know what to do about mac :/
	gamemap()
	player_pos()


def up(ditcioary,inst_replace,inst_player):
	(ditcioary[pos[0]]).pop(pos[1])
	(ditcioary[pos[0]]).insert(pos[1],inst_replace)
	(ditcioary[pos[0]-1]).pop(pos[1])
	(ditcioary[pos[0]-1]).insert(pos[1],inst_player)


def down(ditcioary,inst_replace,inst_player):
	(ditcioary[pos[0]]).pop(pos[1])
	(ditcioary[pos[0]]).insert(pos[1],inst_replace)
	(ditcioary[pos[0]+1]).pop(pos[1])
	(ditcioary[pos[0]+1]).insert(pos[1],inst_player)


def left(ditcioary,inst_replace,inst_player):
	(ditcioary[pos[0]]).pop(pos[1])
	(ditcioary[pos[0]]).insert(pos[1],inst_replace)
	(ditcioary[pos[0]]).pop(pos[1]-1)
	(ditcioary[pos[0]]).insert(pos[1]-1,inst_player)


def right(ditcioary,inst_replace,inst_player):
	(ditcioary[pos[0]]).pop(pos[1])
	(ditcioary[pos[0]]).insert(pos[1],inst_replace)
	(ditcioary[pos[0]]).pop(pos[1]+1)
	(ditcioary[pos[0]]).insert(pos[1]+1,inst_player)



updater()

while True:
	pressedkey = getch()
	if pressedkey is 'w' or pressedkey is 'W':
		if room[pos[0]-1][pos[1]] is not stuff['wall']:
			up(room, stuff['empty'], stuff['player'])
			updater()
			print pos
		else:
			print "Bump! Wall : up"
	elif pressedkey is 's' or pressedkey is 'S':
		if room[pos[0]+1][pos[1]] is not stuff['wall']:
			down(room,stuff['empty'],stuff['player'])
			updater()
			print pos
		else:
			print "Bump! wall : down"
	elif pressedkey is 'a' or pressedkey is 'A':
		if room[pos[0]][pos[1]-1] is not stuff['wall']:
			left(room,stuff['empty'], stuff['player'])
			updater()
			print pos
		else:
			print "Bump! wall : left"
	elif pressedkey is 'd' or pressedkey is 'D':
		if room[pos[0]][pos[1]+1] is not stuff['wall']:
			right(room,stuff['empty'], stuff['player'])
			updater()
			print pos
		else:
			print "Bump! wall : right"