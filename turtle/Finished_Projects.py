#turtle_project.py mka
import turtle
import tkinter as tk
from turtle import *

t = turtle.Turtle()
ts = turtle.Screen()
ts.bgcolor("#67645f")
t.width(1)

#Dice Start

def Natural20(line, spiral, goto, gotonum, distance, tracker): #shape1 and shape 2 should be last, and add a nat 20 dice for cool spell
    ts.clear()
    t = turtle.Turtle()
    ts.bgcolor("#67645f")
    t.speed(10)
    t.penup()
    t.goto(0,50)
    t.setheading(0)
    t.pendown()
    t.color("#a70707")
    for x in range(1): #range change the number of times the code is run
        t.width(5)
        t.left(180 + 30) #directons for movement go here.
        t.fd(50)
        t.left(60)
        t.fd(50)
        t.left(60)
        t.fd(50)
        t.left(60)
        t.fd(50)
        t.left(60)
        t.fd(50)
        t.left(60)
        t.fd(50)
    t.penup()
    t.pendown()
    t.left(90)
    for i in range(1):
        t.fd(line)
        t.left(spiral)
        t.fd(line)
        t.left(spiral)
        t.fd(line)
        t.left(90)#triangle 2 start
        t.fd(line - 35)
        t.right(30)
        t.left(spiral)
        t.fd(line)
        t.left(spiral)
        t.fd(line)
        t.left(spiral)
        t.fd(line)

    t.width(3)#The Two
    t.penup()
    t.color("#ffffff")
    t.goto(-15, 5)
    t.right(90)
    t.pendown()
    for i in range(20):
        t.fd(1)
        t.right(10)
    for i in range(1):
        t.right(15)
        t.fd(20)
        t.left(130)
        t.fd(12)
    t.penup()
    t.goto(8,11)
    t.pendown() #the Zero
    for i in range(10):
        t.right(9.5)
        t.fd(1)
    for i in range(1):
        t.fd(12)
    for i in range(18):
        t.right(10)
        t.fd(1)
    for i in range(1):
        t.fd(13)
    for i in range(5):
        t.right(10)
        t.fd(1)

    t.penup()
    t.goto (50, 50)
#dice end
    t.penup() #star start
    t.color("#1ed3de")
    t.setheading(252)
    for i in range(13): #need a range
        if tracker == 1:
            t.color("#1ed3de")
        elif tracker == 2:
            t.color("#1edec7")
        elif tracker == 3:
            t.color("#1ede5f")
        elif tracker == 4:
            t.color("#89de1e")
        elif tracker == 5:
            t.color("#dade1e")
        elif tracker == 6:
            t.color("#de6f1e")
        elif tracker == 7:
            t.color("#de1e1e")
        elif tracker == 8:
            t.color("#de6f1e")
        elif tracker == 9:
            t.color("#dade1e")
        elif tracker == 10:
            t.color("#89de1e")
        elif tracker == 11:
            t.color("#1ede5f")
        elif tracker == 12:
            t.color("#1edec7")
        elif tracker == 13:
            t.color("#1ed3de")
        t.goto(0, gotonum)
        t.pendown()
        t.fd(distance)
        t.left(180 - 36)
        t.fd(distance)
        t.left(180 - 36)
        t.fd(distance)
        t.left(180 - 36)
        t.fd(distance)
        t.left(180 - 36)
        t.fd(distance)
        t.left(180 - 36)
        gotonum = gotonum + 5
        distance = distance + 10
        tracker = tracker + 1
    t.setheading(180)
    t.color('#ffffff')
    t.circle(300)
    t.penup()
    t.setheading(90)
    t.fd(5)
    t.pendown()
    t.setheading(180)
    t.color('#000000')
    t.circle(305)
    t.penup()
    t.setheading(90)
    t.fd(5)
    t.pendown()
    t.setheading(180)
    t.color("#67645f")
    t.circle(310)

def run():
    Natural20(85, 120, 50, 232.5, 450, 1)


def Nick():
    ts.clear()
    t = turtle.Turtle()
    ts.bgcolor("#ffffff")
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()
    for i in range(600):
        forward(i)
        right(977)
        speed(0)


def Evan():
    ts.clear()
    t = turtle.Turtle()
    ts.bgcolor('#ffffff')
    t.penup()
    t.goto(0,0)
    t.setheading(0)
    t.pendown()
    for x in range(1000):
        forward(x)
        left(1019/2*2.53)
        speed(0)


root = tk.Tk()
root.option_add("*Font", "courier")
root.wm_title("Code Machine")
root.minsize(400, 200)
a = tk.Button(root, text="Mason's code",font=('courier', '20') ,command=run)
b = tk.Button(root, text="Evan's code",font=('courier', '20') ,command=Evan)
c = tk.Button(root, text="Nick's code",font=('courier', '20') ,command=Nick)
t1 = tk.Label(root, text="Not broken, probably.",font=('courier', '10'))
t2 = tk.Label(root, text="Don't start a second process until the first one finishes.",font=('courier', '10'))
a.pack()
b.pack()
c.pack()
t1.pack()
t2.pack()
root.mainloop()



#Natural20(85, 120, 50, 232.5, 450)


holdit = input();
