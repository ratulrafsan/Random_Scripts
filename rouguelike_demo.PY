#@author : Rafsan Ratul (ratulrafsan@gmail.com)
#An attempt to make a simple rouguelike game in python without using any external library

import msvcrt
import os
import random
          # 0   1   2   3   4   5   6   7   8   9  10   11  12  13  14  15
room = {1:['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'], # ^
	    2:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'], # |
	    3:['#','$','.','.','.','.','.','.','.','#','#','#','#','.','.','#'], # |
	    4:['#','.','.','.','.','.','.','#','.','#','.','.','.','.','.','#'], # |
	    5:['#','.','.','.','.','.','@','#','.','#','.','C','#','.','.','#'], # |
	    6:['#','.','.','.','.','.','.','#','.','.','.','.','#','.','.','#'], # x
	    7:['#','.','.','.','.','#','#','#','.','#','#','.','#','.','.','#'], # |
	    8:['#','.','.','.','.','.','.','.','.','.','#','#','#','.','.','#'], # |
	    9:['#','.','.','.','$','.','.','.','.','.','.','.','.','.','.','#'], # |
	   10:['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']} # |
	    # <------------------------------y--------------------------------->

stuff  = {'wall'  :  "#",
          'player':  "@",
          'empty' :  ".",
          'money' :  "$",
          'chest' :  "C"}
potion = ['hp','xp','dmg']
weapon = ['sword','nuclear bomb','TNT']

def chest_choice():
	

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
	os.system('cls')
	gamemap()
	player_pos()


def up(ditcioary,cord_holder,x_cord,y_cord,inst_replace,inst_player):
	(ditcioary[cord_holder[x_cord]]).pop(cord_holder[y_cord])
	(ditcioary[cord_holder[x_cord]]).insert(cord_holder[y_cord],inst_replace)
	(ditcioary[cord_holder[x_cord]-1]).pop(cord_holder[y_cord])
	(ditcioary[cord_holder[x_cord]-1]).insert(cord_holder[y_cord],inst_player)


def down(ditcioary,cord_holder,x_cord,y_cord,inst_replace,inst_player):
	(ditcioary[cord_holder[x_cord]]).pop(cord_holder[y_cord])
	(ditcioary[cord_holder[x_cord]]).insert(cord_holder[y_cord],inst_replace)
	(ditcioary[cord_holder[x_cord]+1]).pop(cord_holder[y_cord])
	(ditcioary[cord_holder[x_cord]+1]).insert(cord_holder[y_cord],inst_player)


def left(ditcioary,cord_holder,x_cord,y_cord,inst_replace,inst_player):
	(ditcioary[cord_holder[x_cord]]).pop(cord_holder[y_cord])
	(ditcioary[cord_holder[x_cord]]).insert(cord_holder[y_cord],inst_replace)
	(ditcioary[cord_holder[x_cord]]).pop(cord_holder[y_cord]-1)
	(ditcioary[cord_holder[x_cord]]).insert(cord_holder[y_cord]-1,inst_player)


def right(ditcioary,cord_holder,x_cord,y_cord,inst_replace,inst_player):
	(ditcioary[cord_holder[x_cord]]).pop(cord_holder[y_cord])
	(ditcioary[cord_holder[x_cord]]).insert(cord_holder[y_cord],inst_replace)
	(ditcioary[cord_holder[x_cord]]).pop(cord_holder[y_cord]+1)
	(ditcioary[cord_holder[x_cord]]).insert(cord_holder[y_cord]+1,inst_player)



updater()

while True:
	pressedkey = msvcrt.getch()
	if pressedkey is 'w' or pressedkey is 'W':
		if room[pos[0]-1][pos[1]] is not stuff['wall']:
			up(room, pos, 0, 1, stuff['empty'], stuff['player'])
			updater()
			print pos
		else:
			print "Bump! Wall : up"
	elif pressedkey is 's' or pressedkey is 'S':
		if room[pos[0]+1][pos[1]] is not stuff['wall']:
			down(room, pos,0,1,stuff['empty'],stuff['player'])
			updater()
			print pos
		else:
			print "Bump! wall : down"
	elif pressedkey is 'a' or pressedkey is 'A':
		if room[pos[0]][pos[1]-1] is not stuff['wall']:
			left(room, pos, 0, 1, stuff['empty'], stuff['player'])
			updater()
			print pos
		else:
			print "Bump! wall : left"
	elif pressedkey is 'd' or pressedkey is 'D':
		if room[pos[0]][pos[1]+1] is not stuff['wall']:
			right(room, pos, 0, 1, stuff['empty'], stuff['player'])
			updater()
			print pos
		else:
			print "Bump! wall : right"