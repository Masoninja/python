#input_abc.py mka
from class_quadratic import *

def main():
	print("Input a, b, and c from an equation in the form of ax^2 = bx + c : ")


	a = float(input("Input a: "))
	b = float(input("Input b: "))
	c = float(input("Input c: "))
	x = float(input("Input x: "))

	p1 = QuadraticEquation(a,b,c)
	x1 = p1.x1()
	x2 = p1.x2()
	print ("Discriminant = ",p1.discriminant())
	print ("x1 = ",x1," x2 = ",x2)
	
	
if __name__ == "__main__":
	main()
