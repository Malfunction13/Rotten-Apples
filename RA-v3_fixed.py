import copy

#take user input for crate size
rowsXcolumns = [input("Please insert your crate size as ROWSxCOLUMNS:")]

#intialize list with crate size in rowsXcolumns format and add the measures as separate list entries by splitting based on "x"
crate_size = []
for measures in rowsXcolumns:
	for measure in measures.split("x"):
		if measure.isnumeric():
			crate_size.append(int(measure))

#strictly for better readability - declare the vars that hold the measures by index number in the list
rows = crate_size[0]
columns = crate_size[1]

#initialazie the 2d matrix based on the dimensions from user input
matrix = [["O" for i in range(columns)] for j in range(rows)]

#function used to print the matrix in more readable format
def Beautify():
	for row in matrix:
		print(*row, sep=" ")

Beautify()

#get the coordinates of the rotten apples from the user, remove unnecessary characters and store in a list as integers
rotten_coordinates = input("Please insert the coordinates of the rotten apples as (X,Y) (X,Y) etc.:")
r_c = rotten_coordinates.replace("(", "").replace(")", "").replace(",", " ")

raw_coordinates = [int(i) for i in r_c.split(" ")]


#now we need to grab coordinate X and coordinate Y and translate them to coordinates applicable to python lists
coordinates_X = raw_coordinates[0::2]
coordinates_Y = raw_coordinates[1::2]

change_A = [(y-1) for y in coordinates_Y]
change_B = [(x-1) for x in coordinates_X]

for a, b in zip(change_A, change_B):
	matrix[a][b] = "X"
Beautify()

#count how many times will the rotting loop run based on the user input of days away
#every 3 days all the adjacent in x.y.z axis apples will rot

t = int(input("Please insert the days away: "))+1

# for every day
for day in range(1, t):
	print('day ' + str(day))

	# need a temp list so we don't influence the result
	temp_matrix = copy.deepcopy(matrix)

	# traverse list from top to bottom
	if ((day % 3) != 0):
		print("No apples have rotten today!")
	else:
		print("Every 3 days adjacent apples rot!")
		for y in range(len(matrix)):
			# traverse list from left to right
			for x in range(len(matrix[y])):
				# check if element is rotten
				if (matrix[y][x] == 'X'):
					# rot all surrounding elements, but check if each element exists first
					if y-1 >= 0:
						if x-1 >= 0:
							temp_matrix[y-1][x-1] = 'X'

						temp_matrix[y-1][x] = 'X'

						if x+1 < len(matrix[y]):
							temp_matrix[y-1][x+1] = 'X'

					if x-1 >= 0:
						temp_matrix[y][x-1] = 'X'

					temp_matrix[y][x] = 'X'

					if x+1 < len(matrix[y]):
						temp_matrix[y][x+1] = 'X'

					if y+1 < len(matrix):
						if x-1 >= 0:
							temp_matrix[y+1][x-1] = 'X'

						temp_matrix[y+1][x] = 'X'

						if x+1 < len(matrix[y]):
							temp_matrix[y+1][x+1] = 'X'

	matrix = copy.deepcopy(temp_matrix)
	Beautify()
