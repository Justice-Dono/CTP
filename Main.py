import turtle
import tkinter as tk
import time

global global_cursor
global_cursor = None

global global_index
global_index = 0

global COMBAT_POSITIONS
COMBAT_POSITIONS = None

global combat_return
combat_return = None

class Hero:
	def __init__(self, name, hp, mp, st, int, speed, lck, items):
		self.name = name
		self.hp = hp
		self.mp = mp
		self.st = st
		self.int = int
		self.speed = speed
		self.lck = lck
		self.items = items

	def damage(self, amount):
		self.hp = self.hp - amount
	
	
	def get_name(self):
		return self.name
	
	def get_hp(self):
		return self.hp
	
	def get_mp(self):
		return self.mp
	
	def get_st(self):
		return self.st
	
	def get_int(self):
		return self.int
	
	def get_speed(self):
		return self.speed
	
	def get_lck(self):
		return self.lck
	
	def get_items(self):
		return self.items

class Monster:
	def __init__(self, name, hp, mp, st, int, lck, speed):
		self.name = name
		self.hp = hp
		self.mp = mp
		self.st = st
		self.int = int
		self.speed = speed
		self.lck = lck

	def damage(self, amount):
		self.hp = self.hp - amount
	
	def get_name(self):
		return self.name
	
	def get_hp(self):
		return self.hp
	
	def get_mp(self):
		return self.mp
	
	def get_st(self):
		return self.st
	
	def get_int(self):
		return self.int
	
	def get_speed(self):
		return self.speed
	
	def get_lck(self):
		return self.lck
	
def window_active(window):
	try:
		window.update()
		return True
	except(turtle.Terminator, tk.TclError):
		return False
	
def move(turtle, index, pos):
	local_position = pos[index]
	turtle.teleport(local_position[0],local_position[1])

def move_up():
    global global_index
    if global_index == 0:
        global_index = 3
    else:
        global_index -= 1
    move(global_cursor, global_index, COMBAT_POSITIONS)

def move_down():
    global global_index
    if global_index == 3:
        global_index = 0
    else:
        global_index += 1
    move(global_cursor, global_index, COMBAT_POSITIONS)

def enter():
	global combat_return
	if(global_index == 0):
		combat_return = "a"
	if(global_index == 1):
		combat_return = "d"
	if(global_index == 2):
		combat_return = "i"
	if(global_index == 3):
		combat_return = "r"

def create_turtle(window, shape):
	local_turtle = turtle.Turtle()
	local_turtle.penup()
	local_turtle.goto(0,0)
	window.addshape(shape)
	local_turtle.shape(shape)
	return local_turtle

def attack(hero, enemy, attacker):
	if attacker == "e":
		hero.damage(enemy.str)

def main():
	global global_cursor
	global COMBAT_POSITIONS
	global combat_return
	game_font = "PressStart2P"
	window = turtle.Screen()
	window.setup(600,600)
	window.title("Combat Window")
	cursor = turtle.Turtle()
	cursor.penup()
	text_turtle= create_turtle(window, "Images/combat-text.gif")
	text_turtle.teleport(-200,-200)
	enemy_turtle = create_turtle(window,"Images/Slime.gif")
	text_x = text_turtle.xcor()
	text_y = text_turtle.ycor()
	COMBAT_POSITIONS = [(text_x-70,text_y+33),(text_x-70, text_y+11.5),(text_x -70, text_y-11),(text_x-70,text_y-34)]
	global_cursor = cursor
	move(cursor, global_index, COMBAT_POSITIONS)
	combat_return = "e"
	update_turtle = turtle.Turtle()
	update_turtle.penup()
	update_turtle.hideturtle()
	update_turtle.goto(200, -100)
	game_font = "PressStart2P"
	main_hero = Hero("Yusha",15,10,5,4,5,10,"Sword")
	monster = Monster("Slime",3,1,1,2,6,3)
	window.listen()
	window.onkey(move_up, "Up")
	window.onkey(move_down, "Down")
	window.onkey(enter, "Return")
	while window_active(window):
		time.sleep(0.001)
		if combat_return == "a":
			update_turtle.write("Attacked!", font=game_font)
			attack(main_hero, monster, "p")
			time.sleep(1.0)
			update_turtle.clear()
			
		if combat_return == "d":
			update_turtle.write("Defended!")
			time.sleep(1.0)
			update_turtle.clear()	
		if combat_return == "i":
			update_turtle.write("Used Item!")
			time.sleep(1.0)
			update_turtle.clear()
		if combat_return == "r":
			update_turtle.write("Ran!")
			time.sleep(1.0)
			update_turtle.clear()
		combat_return = "e"


	try:
		window.bye()
	except Exception:
		pass
	
	

main()

