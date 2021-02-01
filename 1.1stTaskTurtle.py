import turtle, math

turtle.shape('turtle')
turtle.color('green')
n = 3
rad = 20

def regularPolygon(sides, size, turnAr):
	corner = 360/sides
	for x in range(sides):
		turtle.left(corner)
		turtle.forward(size)

	turtle.right(turnAr)
	turtle.penup()
	turtle.forward(20)
	turtle.pendown()
	
for x in range(10):
	size = 2 * rad * math.sin(math.pi / n)
	turnAr = (180 - 360 / n) / 2
	turtle.left(turnAr)
	regularPolygon(n,size,turnAr)
	n += 1 
	rad += 20
turtle.done()
