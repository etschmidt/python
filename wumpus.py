from random import randint

def start_hunt():
	
	#initialize variables
	starting_room = randint(1,21)

	print("""
		You awake in the dread Wumpus lair
		The stench of death in rank in the air
		Hunt the Wumpus; he is hunting you
		Kill the Wumpus, before he kills you!""")

	next_room = input("""
		Which room to go next? """)

start_hunt()