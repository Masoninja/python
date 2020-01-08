'''
Test this.
https://tritech-testsite.smapply.io/

python-circle-list-assignment.py
Get the code: 10.183.1.26 code python
Plot circle data using python
- Use your data
- Change the background color
- Change the graph line colors
- Change the plot line color
- Change the plot dot color
- Label the graph with text Plotting Circumference and Diameter
- Label the axis with text (Circumference and Diameter)
- Upload to github with your name initials or name attached (plot-circle-list-cwc.py)

'''

import turtle
import math
wdth = 800; hgth = 800; bgstring = "#000980"
red = "#cc0000"; green = "#00cc00"; blue = "#00ffff"

def grid(t):
	x = 0; y = 0
	while (x < 400):
		t.speed(0)
		t.penup()
		t.goto(x,y)
		t.pendown()
		t.goto(x,y+400)
		x = x + 100
	x = 0; y = 0
	while (y < 400):
		t.speed(0)
		t.penup()
		t.goto(x,y)
		t.pendown()
		t.goto(x+400,y)
		y = y + 100
		
	t.penup()
	t.goto(0,400)
	t.pendown()
	t.color('#00ffff')
	style = ('Courier', 30, 'bold')
	t.write('Circle Circumference and Diameter Plot', font=("Arial", 15, 'normal', 'bold',))
	t.hideturtle()
	t.penup()
	t.goto(5,-50)
	t.pendown()
	t.color('#00ffff')
	style = ('Courier', 30, 'bold')
	t.write('D i a m e t e r', font=("Arial", 15, 'normal', 'bold',))
	t.hideturtle()
	t.penup()
	t.goto(-30, 80)
	t.pendown()
	t.color('#00ffff')
	style = ('Courier', 30, 'bold')
	t.write('C\n i\n r\n c\n u\n m\n f\n e\n r\n e\n n\n c\n e', font=("Arial", 15, 'normal', 'bold',))
	t.hideturtle()
	t.penup()
	
	
def plotCircles(t):
	#list  named d and c
	d =  [85, 100, 115, 35] 
	c =  [270, 314, 360, 110] 
	# list dsorted and csorted
	dsorted = sorted (d, key = float)
	csorted = sorted(c , key = float)
	t.speed(0)
	t.color('#db3514')
	t.goto(0,0)
	t.pendown()
	t.dot(3, blue)
	t.goto(dsorted[0],csorted[0])
	t.dot(3, blue)
	t.goto(dsorted[1],csorted[1])
	t.dot(3, blue)
	t.goto(dsorted[2],csorted[2])
	t.dot(3, blue)
	t.goto(dsorted[3],csorted[3])
	t.dot(3, blue)
	t.penup()
	t.color(green)
	t.goto(0, 400)
	t.pendown()
	t.goto(400,400)
	t.goto(400, 0)
	
def main():
	try:
		turtle.TurtleScreen._RUNNING = True
		# get wdth and hgth globally
		turtle.screensize(canvwidth=wdth, canvheight=hgth, bg=bgstring)
		print(turtle.Screen().screensize())
		w = turtle.Screen()
		t = turtle.Turtle()
		t.speed(0)
		t.color('#11cf0f')
		t.hideturtle()
		grid(t)
		plotCircles(t)
		w.exitonclick()
	finally:
		turtle.Terminator()
	
if __name__ == '__main__':
	main()

'''
	# Using sorted + key 
	Output = sorted(Input, key = float) 
	# Using sorted + key 
	Output = sorted(Input, key = float) 
'''
