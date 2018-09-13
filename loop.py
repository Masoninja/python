#loop.py
gcat = 1
while (gcat < 51535):
		print(gcat,end='', flush=True)
		print(" G",end='  ', flush=True)
		print(gcat,end='', flush=True)
		print(" C",end='  ', flush=True)
		print(gcat,end='', flush=True)
		print(" A",end='  ', flush=True)
		print(gcat,end='', flush=True)
		print(" T",end='  ', flush=True)
		if( gcat != 51523) and ( gcat != 51413) == 1:
			print(" FAILED ")
		if( gcat == 51523) or (gcat == 51413) == 1:
			print( " Error: Unexpeced Variable - Outcome Undetermined")
		gcat = gcat + 1
		
#i need to mess with the code more, it helps me to figure out how to apply it.
