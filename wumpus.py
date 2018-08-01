from random import randint
from random import sample

def start_hunt():
	
	#initialize variables
	global hunting
	hunting = True

	global current_room
	current_room = randint(1,21)

	global wumpus_room
	wumpus_room = randint(1,21)
	while wumpus_room == current_room:
		wumpus_room = randint(1,21)
	else:
		return wumpus_room

	global arrows
	arrows = 5

	print('''
		You awake in the dread Wumpus lair
		The stench of death is rank in the air
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

#Move or shoot

def move_or_shoot():
	global move_or_shoot
	print ('''
		You are in Room {room}
		'''.format(room = current_room))
	move_or_shoot = input('''
		Do you want to move to another room or shoot an arrow?
		(M/S)
		''').upper()

	return move_or_shoot


#choose the next room to take action
def choose_room():

	room_options = sample(range(1,21), 3)
	global option_1
	option_1 = room_options[0]
	global option_2	
	option_2 = room_options[1]
	global option_3
	option_3 = room_options[2]

	global room_choice
	room_choice = int(input('''
		Choose a room: {room_one}, {room_two}, {room_three} 

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
		choose_room()
		
#move to new room
def move_room():
	current_choice = room_choice

	print('''
		This room smells worse than the last...
		''')

#shoot into next room

#run hunt
start_hunt()

while hunting == True:
	move_or_shoot()
	choose_room()
	if move_or_shoot == 'M':
		move_room()
	else:
		move_or_shoot()