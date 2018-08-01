from random import randint
from random import sample

def start_hunt():
	
	#initialize variables
	global hunting
	hunting = True

	starting_positions = sample(range(1,21), 2)

	global current_room
	current_room = starting_positions[0]

	global wumpus_room
	wumpus_room = starting_positions[1]

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
	global action
	print ('''
		You are in Room {room} and can see tunnels to rooms {room_one}, {room_two}, {room_three}
		You have {arrows} arrows left
		'''.format(room = current_room,
							 room_one=str(option_1), 
							 room_two=str(option_2), 
							 room_three=str(option_3),
							 arrows=str(arrows)
							)
				)
	action = input('''
		Do you want to move to another room or shoot an arrow?
		(M/S)
		''').upper()

#choose the next room to take action
def choose_room():

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
	current_room = room_choice

	print('''
		You are now in Room {room}
		This room smells worse than the last...
		'''.format(room = current_room))

#shoot into next room
def shoot_arrow():
	
	arrows =- 1
	print('''
		The arrow falls to the ground
		''')

#run hunt
start_hunt()
set_room_options()
while hunting == True:

	move_or_shoot()
	choose_room()
	if action == 'M':
		move_room()
	elif action == 'S':
		shoot_arrow()
	else:
		print('Invalid action')

else:
	print('''
		Game over, man
		''')