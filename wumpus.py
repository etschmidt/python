from random import randint

def start_hunt():
	
	#initialize variables
	current_room = randint(1,21)

	print("""
		You awake in the dread Wumpus lair
		The stench of death in rank in the air
		Hunt the Wumpus; he is hunting you;
		Kill the Wumpus, ere he kills you!
		""")

#choose the next room to move
def choose_room():

	option_1 = randint(1,21)
	option_2 = randint(1,21)
	option_3 = randint(1,21)

	room_choice = int(input("""
		Which room to go next? {room_one}, {room_two}, {room_three}
		""".format(room_one=str(option_1), 
							 room_two=str(option_2), 
							 room_three=str(option_3)
							)
		))

	if room_choice in [option_1, option_2, option_3]:
		current_room = room_choice 
	else:
		print("""
			invalid room choice
			""")

#move to new room
def move_room():
	current_room = room_choice

#run hunt
start_hunt()

choose_room()