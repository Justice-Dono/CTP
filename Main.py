import turtle
import tkinter as tk
import time


def window_active(window):
	try:
		window.update()
		return True
	except(turtle.Terminator, tk.TclError):
		return False
	
def main():
	window = turtle.Screen()
	window.setup(400,400)
	window.title("Combat Window")
	combat_turtle = turtle.Turtle()
	#combat_turtle.hideturtle()
	combat_turtle.penup()
	combat_turtle.goto(0, 0)
	style = ("Arial", 36, "bold")
	combat_turtle.write("Hello World", align="center", font=style)
	window.addshape("cat-laptop.gif")
	cat_turtle = turtle.Turtle()
	cat_turtle.penup()
	cat_turtle.goto(0,0)
	cat_turtle.shape("cat-laptop.gif")
	step = 20

	def move(dx, dy):
		try:
			x, y = combat_turtle.position()
			combat_turtle.clear()
			combat_turtle.goto(x + dx, y + dy)
			combat_turtle.write("Hello World", align="center", font=style)

			window.update()
		except (turtle.Terminator, tk.TclError):
			pass

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

