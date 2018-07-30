# https://www.digitalocean.com/community/tutorials/how-to-make-a-simple-calculator-program-in-python-3

def calculate():

	#inputs
	number_1 = int(input("Enter your first number:  "))

	operation = input('''
		Type the operation you wish to complete:
	''')

	number_2 = int(input("Enter your second number:  "))

	# Addition
	if operation == '+':
		print('{} + {} = '.format(number_1, number_2))
		print(number_1 + number_2)

	# Subtraction
	elif operation == '-':
		print('{} - {} = '.format(number_1, number_2))
		print(number_1 - number_2)

	# Multiplication
	elif operation == '*':
		print('{} * {} = '.format(number_1, number_2))
		print(number_1 * number_2)

	# Division
	elif operation == '/':
		print('{} / {} = '.format(number_1, number_2))
		print(number_1 / number_2)

	else: 
		print("invalid operation, fuckhead")
		calculate()

	again()

def again():

	calc_again = input('''
		Go again? (Y/N)
	''')

	if calc_again.upper() == 'Y':
		calculate()
	elif calc_again.upper() == 'N':
		print('GTFO')
	else:
		again()

#call the function
calculate()