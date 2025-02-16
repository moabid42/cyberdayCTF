from common import num_mazes, origin, target, move
from queue import PriorityQueue


host = 'localhost'
port = 8447


def solve(maze, start, end):
	'''
	Returns the optimal cost and the solution to traverse the maze.
	Parameters:
		- maze: a 2D-array of bytes, possible elements: origin, target, empty, wall
		- start: a set of (x, y) coorinates
		- end: a set of (x, y) coorinates
	'''
	unvisited_cost = 10**10
	# maze of (cost, origin, pos, move_to_get_here)
	solution = [[(unvisited_cost, None, (col, row), None) for col in range(len(maze[0]))] for row in range(len(maze))]
	solution[start[1]][start[0]] = (0, None, start, None)
	q = PriorityQueue()
	q.put(solution[start[1]][start[0]])
	while not q.empty():
		cost, origin, pos, prev_move = q.get()
		# Process the current position
		if cost <= solution[pos[1]][pos[0]][0]:
			solution[pos[1]][pos[0]] = (cost, origin, pos, prev_move)
		else:
			continue
		# test each possible move
		for _move in b'12345678udlr':
			# test if the move is possible
			_move = _move.to_bytes(1, 'little')
			move_results = move(maze, pos, _move)
			if move_results is None:
				continue
			new_pos, additional_cost = move_results
			new_cost = cost + additional_cost
			# test if the move is an improvement to reach new_pos
			if new_cost < solution[new_pos[1]][new_pos[0]][0]:
				solution[new_pos[1]][new_pos[0]] = (new_cost, pos, new_pos, _move)
				q.put(solution[new_pos[1]][new_pos[0]])
	# reconstruct path:
	path = b''
	pos = end
	if solution[pos[1]][pos[0]][1] is None:
		return None
	while solution[pos[1]][pos[0]][1] is not None:
		#print('Solution-path:', solution[pos[1]][pos[0]])
		path = (solution[pos[1]][pos[0]][3] if solution[pos[1]][pos[0]][3] is not None else b'') + path
		pos = solution[pos[1]][pos[0]][1]
	return solution[end[1]][end[0]][0], path


def main():
	# Connect to the challenge:
	conn = remote(host, port)
	# Read the intro
	for _ in range(15):
		print(conn.recvline().decode().strip())
	# Solve the levels:
	for _ in range(num_mazes):
		print(conn.recvline().decode().strip()) # "Level"
		data = conn.recvuntil(b'Please submit your sequence of moves: ').decode().split('\r\n')
		#print('\r\n'.join(data[:-1])) # Print maze
		print(data[-1], end='') # 'Please submit your sequence of moves: '
		maze = [row.encode('cp437') for row in data[:-1]]
		for row in range(len(maze)):
			for col in range(len(maze[0])):
				if maze[row][col].to_bytes(1, 'little') == target:
					end = (col, row)
				elif maze[row][col].to_bytes(1, 'little') == origin:
					start = (col, row)
		optimal_cost, movement = solve(maze, start, end)
		print(movement.decode())
		conn.writeline(movement)
		result = conn.recvline().decode().strip()
		assert result == 'Correct!'
		print(result)
	# Read the epilogue:
	print(conn.recvline().decode().strip())
	print(conn.recvline().decode().strip())
	# Close the connection to the challenge:
	conn.close()


if __name__ == '__main__':
	from pwn import remote # pip install pwntools
	for i in range(200):
		print('='*60 + str(i) + '='*60)
		main()
