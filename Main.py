import turtle
import tkinter as tk
import time

global global_cursor
global_cursor = None

global global_index
global_index = 0

global COMBAT_POSITIONS
COMBAT_POSITIONS = None

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
	print(global_index)

def create_turtle(window, shape):
	local_turtle = turtle.Turtle()
	local_turtle.penup()
	local_turtle.goto(0,0)
	window.addshape(shape)
	local_turtle.shape(shape)
	return local_turtle

def main():
	global global_cursor
	global COMBAT_POSITIONS
	window = turtle.Screen()
	window.setup(600,600)
	window.title("Combat Window")
	cursor = turtle.Turtle()
	#combat_turtle.hideturtle()
	cursor.penup()
	text_turtle= create_turtle(window, "Images/combat-text.gif")
	text_turtle.teleport(-200,-200)
	text_x = text_turtle.xcor()
	text_y = text_turtle.ycor()
	COMBAT_POSITIONS = [(text_x-70,text_y+33),(text_x-70, text_y+11.5),(text_x -70, text_y-11),(text_x-70,text_y-34)]
	global_cursor = cursor
	move(cursor, global_index, COMBAT_POSITIONS)



	window.listen()
	window.onkey(move_up, "Up")
	window.onkey(move_down, "Down")
	window.onkey(enter, "Return")
	while window_active(window):
		time.sleep(0.001)

	try:
		window.bye()
	except Exception:
		pass
	
	

main()

