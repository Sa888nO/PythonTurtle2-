import turtle

turtle.shape('turtle')
turtle.color('green')
stat = 0.5;

def circle(n):
	global stat
	turtle.left(90)
	for y in range(n):
		for x in range(360):
			turtle.forward(stat)
			turtle.right(1)
		turtle.right(180)
		for x in range(360):
			turtle.forward(stat)
			turtle.right(1)
		stat += 0.1
circle(int(input('Кол-во витков: ')))
turtle.hideturtle()
turtle.done()