#turtle_project.py mka
import turtle
import Tkinter as tk

t = turtle.Turtle()
ts = turtle.Screen()
ts.bgcolor("#67645f")
t.width(10)

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



def run():
    Natural20(85, 120, 50, 232.5, 450, 1)


root = tk.Tk()
root.option_add("*Font", "courier")
root.wm_title("Code Machine")
root.minsize(400, 200)
a = tk.Button(root, text="Roll D20",font=('courier', '20') ,command=run)
t1 = tk.Label(root, text="Not broken, probably.",font=('courier', '10'))
a.pack()
t1.pack()
root.mainloop()



#Natural20(85, 120, 50, 232.5, 450)


holdit = input();
