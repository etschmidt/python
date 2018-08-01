# Intro to Programming Using Python - Assignment #1
# Completed by: Ethan T. Schmidt

# 1. Print out the following text: 
# You've reached [your name]. 
# I'm not available right now, so leave a message and I'll call you back.

def ansering_machine():
	global my_name
	my_name = "ethan"
	print("""
		You've reached {name}.
		I'm not available right now, so leave a message and I'll call you back.
		""".format(name=my_name))

ansering_machine()

# 2. Create five variables for your first name, last name, shoe size, height, and age. 
# And then print them out on one line.

def my_info():
	first_name = "ethan"
	last_name = "schmidt"
	size = "9.5"
	height = "5\'10\""
	age = "30"
	print("""
		{first_name} {last_name} {size} {height} {age}
		""".format(first_name=first_name, last_name=last_name, size=size, height=height, age=age)
	)

my_info()

# 3. If subtotal = 10.58 and tip = 0.22 (22%) then calculate the total bill amount
# in a variable named total and print it out.

def tip_calc():
	subtotal = 10.58
	tip = 0.22
	global total
	total = subtotal * (1 + tip)
	print(total)

tip_calc()

# 4. Convert 158.8 into an integer. 
# Convert 75 into a float. 
# Convert "244.9" into a float and then an integer.

def convert():
	print(int(158.8))
	print(float(75))
	print(int(float(244.9)))

convert()

# 5. Use \t and \n in a string and then print it out so that it matches (approximately) the following:
# -in the woods
#               which
#                   stutter
#                           and
# 
#                               sing

def poem():
	print("""
	-in the woods
	\t\twhich
	\t\t\tstutter
	\t\t\t\tand\n
	\t\t\t\t\tsing""")

poem()

# 6. Put your first name and total from above into an f-string (f"...") so that it reads: 
# Mattan, your total is $12.91 
# (remember to round the total to the nearest cent)


def fstring():
	print(f'{my_name}, your total is {total}')

fstring()

# 7. Use input() to ask a user for the city they live in, and then print it back to them.

def city():
	city = input("""
		what city do you live in?
		""")
	print(f'{city}')

city()

# 8. Build a future value calculator by using input() to get values from the user. 
# (Make sure you convert them into integers or floats before doing any math on them.) 
# Print out the result.
# Hint: Future Value = Present Value x (1 + rate of return) ^ number of periods

def future_calc():
	present_value = float(input("Present Value: "))
	rate_of_return = float(input("Rate of Return: "))
	periods = float(input("Number of Periods: "))

	future_value = present_value * ((1 + rate_of_return) ** periods)

	print(future_value)

future_calc()