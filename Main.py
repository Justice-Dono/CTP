import turtle
import tkinter as tk
import time


def window_active(window):
	try:
		window.update()
		return True
	except(turtle.Terminator, tk.TclError):
		return False
	
def move(turtle, index, pos):
	local_position = pos[index]
	turtle.teleport(local_position[0],local_position[1])
	
def create_turtle(window, shape):
	local_turtle = turtle.Turtle()
	local_turtle.penup()
	local_turtle.goto(0,0)
	window.addshape(shape)
	local_turtle.shape(shape)
	return local_turtle

def main():
	window = turtle.Screen()
	window.setup(600,600)
	window.title("Combat Window")
	combat_turtle = turtle.Turtle()
	#combat_turtle.hideturtle()
	combat_turtle.penup()
	text_turtle= create_turtle(window, "Images/combat-text.gif")
	text_turtle.teleport(-200,-200)
	text_x = text_turtle.xcor()
	text_y = text_turtle.ycor()
	COMBAT_POSITIONS = [(text_x-70,text_y+33),(text_x-70, text_y+11.5),(text_x -70, text_y-11),(text_x-70,text_y-34)]
	test = COMBAT_POSITIONS[0]
	combat_index = 0
	test = COMBAT_POSITIONS[combat_index]
	combat_turtle.teleport(test[0],test[1])

	
		

	def move_up():
		move(0, step)

	def move_down():
		move(0, -step)

	def move_left():
		move(-step, 0)

	def move_right():
		move(step, 0)


	window.listen()
	window.onkey(move_up, "Up")
	window.onkey(move_down, "Down")
	window.onkey(move_left, "Left")
	window.onkey(move_right, "Right")

	while window_active(window):
		time.sleep(0.001)

	try:
		window.bye()
	except Exception:
		pass
	
	

main()

