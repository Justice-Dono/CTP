import turtle


def main():
	window = turtle.Screen()
	window.title("Combat Window")

	combat_turtle = turtle.Turtle()
	combat_turtle.hideturtle()
	combat_turtle.penup()
	combat_turtle.goto(0, 0)
	style = ("Arial", 36, "bold")
	combat_turtle.write("Hello World", align="center", font=style)

	window.exitonclick()


if __name__ == "__main__":
	main()

