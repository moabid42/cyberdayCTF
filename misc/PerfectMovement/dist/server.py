#!/usr/bin/python3


import os
import time
import random
from common import num_mazes, origin, target, empty, wall, move
try:
	# Of course, you don't get the solve-script...
	from solver import solve
except Exception as e:
	# have a dummy implementation that instead returns some value bigger than the optimal cost:
	def solve(maze, start, end):
		'''
		Returns 
			- either the optimal cost and the solution to traverse the maze
			- or None, if the maze is not solvable.
		Parameters:
			- maze: a 2D-array of bytes, possible elements: origin, target, empty, wall
			- start: a set of (x, y) coorinates
			- end: a set of (x, y) coorinates
		'''
		optimal_cost = 10**10
		solution = None
		return (optimal_cost, solution)


# Constants
time_limit_in_seconds = 2 * num_mazes # The time limit for the challenge
size_factor = 15
wall_probability = 0.5


def generate_maze(level):
	'''
	Generates and returns
		- the randomly generated maze,
		- the starting position,
		- the target position
		- and the optimal cost.
	'''
	# Maze size
	min = size_factor * level
	max = size_factor * (level + 1)
	width = random.randrange(min, max)
	height = random.randrange(min, max)
	# Chose the start and end close to the rim:
	start_offset = random.randrange(0, 5)
	end_offset = random.randrange(0, 5)
	# Chose any of 4 directions: left <-> right / top <-> bottom
	direction = random.randrange(0, 2)
	if random.randrange(0, 2) == 0:
		# direction: left <-> right
		start = (start_offset if direction == 0 else (width - 1 - start_offset),  random.randrange(0, height))
		end   = ((width - 1 - end_offset) if direction == 0 else end_offset, random.randrange(0, height))
	else:
		# direction: top <-> bottom
		start = (random.randrange(0, width), start_offset if direction == 0 else (height - 1 - start_offset))
		end   = (random.randrange(0, width), (height - 1 - end_offset) if direction == 0 else end_offset)
	# "solution" can be None, in case the randomly generated maze can not be solved. Regenerate the maze until it is solvable:
	solution = None
	while solution is None:
		# Setup maze
		maze = [[wall if random.random() < wall_probability else empty for _ in range(width)] for _ in range(height)]
		maze[start[1]][start[0]] = origin
		maze[end[1]][end[0]] = target
		# Verify the solvability of maze and compute the optimal cost:
		solution = solve(maze, start, end)
	return maze, start, end, solution[0]


def single_maze(level):
	'''
	Run one level.
	'''
	maze, pos, end, optimal_cost = generate_maze(level)
	cost = 0
	# Print the maze
	print(f'Level {level}:', end='\r\n')
	for row in maze:
		print(b''.join(row).decode('cp437'), end='\r\n')
	path = input('Please submit your sequence of moves: ')
	# Simulate the moves
	for _move in path:
		res = move(maze, pos, bytes([ord(_move)]))
		# check for invalid move
		if res is None:
			return False
		pos = res[0]
		cost += res[1]
	# Check if the target position has been reached and the cost is optimal.
	return pos == end and cost <= optimal_cost


def main():
	'''
	Run the challenge.
	'''
	print(b'''Traverse the following mazes most efficiently starting at [O] with the target being [X]. [ ] marks an empty tile, whereas [\xDB] marks a blocked tile which you can not move to. You have several movement options:
At the cost of 5 each, you can perform the following movements:
[1] Move up two tiles and one tile to the right
[2] Move up one tile and two tiles to the right
[3] Move down one tile and two tiles to the right
[4] Move down two tiles and one tile to the right
[5] Move down two tiles and one tile to the left
[6] Move down one tile and two tiles to the left
[7] Move up one tile and two tiles to the left
[8] Move up two tiles and one tile to the left
At the cost of 2 each, you can perform the following movements:
[u] Move up one tile
[d] Move down one tile
[l] Move left one tile
[r] Move right one tile'''.decode('cp437'), end='\r\n')
	start_time = time.time()
	for level in range(num_mazes):
		if not single_maze(level + 1):
			print('You did not solve the maze. Try again, once you have improved you skills.', end='\r\n')
			return
		# check time constraint
		end_time = time.time()
		duration_in_seconds = end_time - start_time
		if duration_in_seconds > time_limit_in_seconds:
			print('You have been too slow. Try again, once you have improved you skills.', end='\r\n')
			return
		print('Correct!', end='\r\n')
	print(f'It took you {duration_in_seconds} seconds to solve the challenge.', end='\r\n')
	flag = os.environ.get('FLAG') or '42HN{fake_flag}'
	print('Congratulations, here\'s your flag:', flag, end='\r\n')
	return


if __name__ == '__main__':
	main()
