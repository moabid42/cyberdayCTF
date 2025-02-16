# Constants
num_mazes = 20
# Characters for the maze representation
origin = b'O'
target = b'X'
empty  = b' '
wall   = b'\xDB'


def move(maze, pos, _move):
	'''
	Attempt to move.
	Returns the new position and the cost associated with that move, if the move is valid; returns None otherwise.
	'''
	if   _move == b'1' or _move == '1':
		dx = +1
		dy = -2
	elif _move == b'2' or _move == '2':
		dx = +2
		dy = -1
	elif _move == b'3' or _move == '3':
		dx = +2
		dy = +1
	elif _move == b'4' or _move == '4':
		dx = +1
		dy = +2
	elif _move == b'5' or _move == '5':
		dx = -1
		dy = +2
	elif _move == b'6' or _move == '6':
		dx = -2
		dy = +1
	elif _move == b'7' or _move == '7':
		dx = -2
		dy = -1
	elif _move == b'8' or _move == '8':
		dx = -1
		dy = -2
	elif _move == b'u' or _move == 'u':
		dx = +0
		dy = -1
	elif _move == b'd' or _move == 'd':
		dx = +0
		dy = +1
	elif _move == b'l' or _move == 'l':
		dx = -1
		dy = +0
	elif _move == b'r' or _move == 'r':
		dx = +1
		dy = +0
	else:
		# Invalid move
		return None
	new_pos = (pos[0] + dx, pos[1] + dy)
	# Check for maze boundaries
	if new_pos[0] < 0 or new_pos[0] >= len(maze[0]) or new_pos[1] < 0 or new_pos[1] >= len(maze):
		return None
	# Can not move onto a wall tile
	if maze[new_pos[1]][new_pos[0]] == wall or maze[new_pos[1]][new_pos[0]] == ord(wall):
		return None
	cost = 5 if _move <= b'8' else 2
	return new_pos, cost
