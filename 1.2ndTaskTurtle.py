import turtle

turtle.shape('turtle')
turtle.color('green')

def circle(n):
	corner = 360/n
	for y in range(n):
		turtle.right(corner)
		for x in range(360):
			turtle.forward(1)
			turtle.right(1)
circle(int(input()))
turtle.hideturtle()
turtle.done()