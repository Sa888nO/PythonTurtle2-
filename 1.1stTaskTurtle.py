import turtle

turtle.shape('turtle')
turtle.color('green')
n = 2
step = 15

def regularPolygon():
	global n
	global step
	n += 1 
	step += 15
	for x in range(n):
		turtle.left(360/n)
		turtle.forward(step)
	turtle.right(45)
	turtle.penup()
	turtle.forward(15)
	turtle.left(45)
	turtle.pendown()
	
for x in range(10):
	regularPolygon()
turtle.done()