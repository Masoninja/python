#diamond.py mka
import math
import turtle
w = turtle.Screen()
w.bgcolor("black")
t = turtle.Turtle()
t.color("orange")
t.speed(0)
#the input should be 50 for size
def diamond(size):
	for i in range(10):
		t.color("orange")
		t.left(90)
		t.fd(size)
		t.left(135)
		t.fd(math.sqrt((size ** 2) * 2))
		t.right(90 + 135)
		t.fd(size * 2)
		t.right(135)
		t.fd(math.sqrt((size ** 2) * 2))
		t.left(135 + 90)
		t.fd(size * 2)
		t.goto(0,0)
		t.color("yellow")
		t.left(90)
		t.fd(size)
		t.left(135)
		t.fd(math.sqrt((size ** 2) * 2))
		t.right(90 + 135)
		t.fd(size * 2)
		t.right(135)
		t.fd(math.sqrt((size ** 2) * 2))
		t.left(135 + 90)
		t.fd(size * 2)
		size = size + 5
		t.goto(0,0)
		            #loop number 2 starts here
		t.color("yellow")
		t.left(90)
		t.fd(size)
		t.left(135)
		t.fd(math.sqrt((size ** 2) * 2))
		t.right(90 + 135)
		t.fd(size * 2)
		t.right(135)
		t.fd(math.sqrt((size ** 2) * 2))
		t.left(135 + 90)
		t.fd(size * 2)
		t.goto(0,0)
		t.color("orange")
		t.left(90)
		t.fd(size)
		t.left(135)
		t.fd(math.sqrt((size ** 2) * 2))
		t.right(90 + 135)
		t.fd(size * 2)
		t.right(135)
		t.fd(math.sqrt((size ** 2) * 2))
		t.left(135 + 90)
		t.fd(size * 2)
		t.goto(0,0)
		size = size + 5
		
		
diamond(50)

def star(size):
	for i in range(10):
		t.goto (0,0)
		t.color("red")
		t.left(90)
		t.right(size - 5)
		t.fd(size * 2)
		size = size + 10
		
		
star(50)
	
holdit = input()
