import random

num_of_queens = 8

#board = [ [0] * num_of_queens ] * num_of_queens
#board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
board = [[0] * num_of_queens]
i = 1
while i < num_of_queens:
	board.append([0] * num_of_queens)
	i += 1
queen_position = []



#for line in board:
#	print(line)


# Place queens on board, one per row, one per column
# Try randomly first
avail_row = []
avail_col = []
i = 0
while i < num_of_queens:
	avail_row.append(i)
	avail_col.append(i)
	i += 1
while len(avail_row) > 0:
	a = random.randint(0, len(avail_row) - 1)
	b = random.randint(0, len(avail_col) - 1)
	queen_position.append([avail_row[a], avail_col[b]])
	board[avail_row[a]][avail_col[b]] = 1
	avail_row.pop(a)
	avail_col.pop(b)

for line in board:
	print(line)

i = 0
while i < len(queen_position):
	j = i + 1
	while j < len(queen_position):
		a = queen_position[i][0]
		b = queen_position[i][1]
		while a > -1 and b > -1:
			a -= 1
			b -= 1
			if a == queen_position[j][0] and b == queen_position[j][1]:
				print("Collision between " + str(queen_position[i]) + " and " + str(queen_position[j]))
		a = queen_position[i][0]
		b = queen_position[i][1]
		while a > -1 and b < num_of_queens + 1:
			a -= 1
			b += 1
			if a == queen_position[j][0] and b == queen_position[j][1]:
				print("Collision between " + str(queen_position[i]) + " and " + str(queen_position[j]))
		a = queen_position[i][0]
		b = queen_position[i][1]
		while a < num_of_queens + 1 and b > -1:
			a += 1
			b -= 1
			if a == queen_position[j][0] and b == queen_position[j][1]:
				print("Collision between " + str(queen_position[i]) + " and " + str(queen_position[j]))
		a = queen_position[i][0]
		b = queen_position[i][1]
		while a < num_of_queens + 1 and b < num_of_queens + 1:
			a += 1
			b += 1
			if a == queen_position[j][0] and b == queen_position[j][1]:
				print("Collision between " + str(queen_position[i]) + " and " + str(queen_position[j]))
		j += 1
	i += 1