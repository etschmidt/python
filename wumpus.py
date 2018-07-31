from random import randint
from random import sample

def start_hunt():
	
	#initialize variables
	current_room = randint(1,21)

	print('''
		You awake in the dread Wumpus lair
		The stench of death in rank in the air
		Hunt the Wumpus; he is hunting you;
		Kill the Wumpus, ere he kills you!
		''')

# initialize room options
def set_room_options():
	room_options = sample(range(1,21), 3)
	global option_1
	option_1 = room_options[0]
	global option_2	
	option_2 = room_options[1]
	global option_3
	option_3 = room_options[2]

#choose the next room to move
def choose_room():

	global room_choice
	room_choice = int(input('''
		Which room to go next? {room_one}, {room_two}, {room_three}
		'''.format(room_one=str(option_1), 
							 room_two=str(option_2), 
							 room_three=str(option_3)
							)
		))

	if room_choice in [option_1, option_2, option_3]: 
		return room_choice
	else:
		print('''
			Invalid room choice \
			''')
		
#move to new room
def move_room():
	current_choice = room_choice

	print('''
		This room smells worse than the last...
		''')

#run hunt
start_hunt()

set_room_options()

choose_room()
