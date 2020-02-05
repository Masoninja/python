from mcpi.minecraft import Minecraft
from mcpi import block
from   time import sleep
from random import randint 

def init():
 #ipString = "192.168.1.73"
 ipString = "127.0.0.1"
 #mc = Minecraft.create("127.0.0.1", 4711)
 mc = Minecraft.create(ipString, 4711)
 mc.setting("world_immutable",True)
 #x, y, z = mc.player.getPos()  
 return mc
 
 
 
def dirt(mc,x,y,z):
	dirtcount = 0
	rowcount = 0
	mc.postToChat("Crimson - randomized grass!")
	while(rowcount <= 16):
		dirtcolor = randint(0,5)
		print(str(dirtcolor))
		if(dirtcolor == 0):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 3)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 35, 13) #grass
		elif(dirtcolor == 1):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 5)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 103) #grass
		elif(dirtcolor == 2):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 17)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 35, 5) #grass
		elif(dirtcolor == 3):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 1)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 18, 1) #grass
		elif(dirtcolor == 4):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 3)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 18, 3) #grass
		elif(dirtcolor == 5):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 35, 12)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 35, 5) #grass
		dirtcount = (dirtcount + 1)
		if(dirtcount >= 16):
			rowcount = (rowcount + 1)
			dirtcount = 0

def talk(mc):
	mc.postToChat("Every time this code is run, the grass block turns out different!")
	
def block2(mc,x,y,z):
	dirtcount = 0
	rowcount = 0
	mc.postToChat("you can compare four different blocks here!")
	while(rowcount <= 16):
		dirtcolor = randint(0,5)
		print(str(dirtcolor))
		if(dirtcolor == 0):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 3)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 35, 13) #grass
		elif(dirtcolor == 1):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 5)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 103) #grass
		elif(dirtcolor == 2):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 17)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 35, 5) #grass
		elif(dirtcolor == 3):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 1)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 18, 1) #grass
		elif(dirtcolor == 4):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 3)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 18, 3) #grass
		elif(dirtcolor == 5):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 35, 12)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 35, 5) #grass
		dirtcount = (dirtcount + 1)
		if(dirtcount >= 16):
			rowcount = (rowcount + 1)
			dirtcount = 0	 
		


def block3(mc,x,y,z):
	dirtcount = 0
	rowcount = 0
	while(rowcount <= 16):
		dirtcolor = randint(0,5)
		print(str(dirtcolor))
		if(dirtcolor == 0):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 3)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 35, 13) #grass
		elif(dirtcolor == 1):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 5)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 103) #grass
		elif(dirtcolor == 2):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 17)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 35, 5) #grass
		elif(dirtcolor == 3):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 1)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 18, 1) #grass
		elif(dirtcolor == 4):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 3)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 18, 3) #grass
		elif(dirtcolor == 5):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 35, 12)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 35, 5) #grass
		dirtcount = (dirtcount + 1)
		if(dirtcount >= 16):
			rowcount = (rowcount + 1)
			dirtcount = 0	


def block4(mc,x,y,z):
	dirtcount = 0
	rowcount = 0
	while(rowcount <= 16):
		dirtcolor = randint(0,5)
		print(str(dirtcolor))
		if(dirtcolor == 0):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 3)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 35, 13) #grass
		elif(dirtcolor == 1):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 5)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 103) #grass
		elif(dirtcolor == 2):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 17)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 35, 5) #grass
		elif(dirtcolor == 3):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 1)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 18, 1) #grass
		elif(dirtcolor == 4):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 3)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 18, 3) #grass
		elif(dirtcolor == 5):
			if(rowcount <= 12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 35, 12)
			elif(rowcount >12):
				mc.setBlock((x + dirtcount), (y + rowcount), z, 35, 5) #grass
		dirtcount = (dirtcount + 1)
		if(dirtcount >= 16):
			rowcount = (rowcount + 1)
			dirtcount = 0

def main():
 mc = init()
 x,y,z = mc.player.getPos()
 mc.player.setPos(x,y,z)
 dirt(mc,x,y,z)
 mc.player.setPos(x+17,y,z)
 talk(mc)
 x,y,z = mc.player.getPos()
 block2(mc,x,y,z)
 mc.player.setPos(x-17,y+18,z)
 x,y,z = mc.player.getPos()
 block3(mc,x,y,z)
 mc.player.setPos(x+17,y,z)
 x,y,z = mc.player.getPos()
 block4(mc,x,y,z)
 mc.player.setPos(x, y+5, z+10)
 

if __name__ == "__main__":
 main()
