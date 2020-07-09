#!/usr/bin/env python3

# Define placeholder char
EMPTY_MARKER = '*'

class OXs (object):
	def __init__(self, player_marker, ai_marker):
		self._player_marker = player_marker
		self._ai_marker = ai_marker
		self._winner = ''
		self._board = self.set_board()
		self._current_marker = player_marker

	#	Board design
	#	1 | 2 | 3
	#	---------
	#	4 | 5 | 6
	#	---------
	#	7 | 8 | 9
	#	Positions stored in list 0-8 / Access by list[pos-1]
		
	def set_board(self) -> list:
		board = [EMPTY_MARKER] * 9
		return board
		
	def play_turn(self, pos) -> bool:
		is_valid = self.within_range(pos) and not self.is_occupied(pos)
		if is_valid:
			self._board[pos-1] = self._current_marker
			# Flip the turn from ai to player, or player to ai
			self._current_marker = self._ai_marker if self._player_marker \
			else self._player_marker
		return is_valid # Allows us to check if turn was valid

	# Check if a played turn is within range (1-9)
	def within_range(self, number):
		return 0 < number <= len(self._board)

	# Check if a position is taken
	# [char other than placeholder found]
	def is_occupied(self, pos):
		return self._board[pos-1] != EMPTY_MARKER
	
	# Display the current game board
	def print_board(self):
		print('\n')
		for i in range(len(self._board)):
			if i % 3 == 0 and i != 0:
				print('\n ------------ ')
			print(f' | {self._board[i]}', end ='')
		print('\n')

	# Print a guide board for the user showing positions 1-9
	def print_board_template(self):
		print('\n')
		for i in range(len(self._board)):
			if i % 3 == 0 and i != 0:
				print('\n ------------ ')
			print(f' | {i+1}', end ='')
		print('\n')	

	# Check for a winner
	def is_there_a_winner(self):
		# Check lef/right diagonals and middle row/column for a winning line
		diagonals_and_middles = (self.right_diag() or self.left_diag() \
		or self.middle_row() or self.second_col()) \
		and self._board[4] != EMPTY_MARKER
		# Check top row and first column for a winning line
		top_and_first = (self.top_row() or self.first_col()) \
		and self._board[0] != EMPTY_MARKER
		# Check bottom row and last column for a winning line
		bottom_and_last = (self.bottom_row() or self.last_col()) \
		and self._board[8] != EMPTY_MARKER
		# If a winning line was found record the winning character (e.g. X or O)
		if diagonals_and_middles:
			self._winner = self._board[4]
		elif top_and_first:
			self._winner = self._board[0]
		elif bottom_and_last:
			self._winner = self._board[8]
		# Return true if winning line found
		return diagonals_and_middles or top_and_first or bottom_and_last

	# Define right diagonal
	def right_diag(self):
		return self._board[0] == self._board[4] == self._board[8]

	# Define left diagonal
	def left_diag(self):
		return self._board[2] == self._board[4] == self._board[6]

	# Define top row
	def top_row(self):
		return self._board[0] == self._board[1] == self._board[2]

	# Define middle row
	def middle_row(self):
		return self._board[3] == self._board[4] == self._board[5]	
	
	# Define bottom row
	def bottom_row(self):
		return self._board[6] == self._board[7] == self._board[8]

	# Define fist column
	def first_col(self):
		return self._board[0] == self._board[3] == self._board[6]

	# Define second column
	def second_col(self):
		return self._board[1] == self._board[4] == self._board[7]
	
	# Define last column
	def last_col(self):
		return self._board[2] == self._board[5] == self._board[8]

	# Check if board is full
	def is_the_board_full(self):
		for i in range(len(self._board)):
			if self._board[i] == EMPTY_MARKER:
				return False
		return True

	def game_over(self):
		did_someone_win = self.is_there_a_winner()
		if did_someone_win:
			return 'We have a winner! The winner is ' + self._winner \
			+ 's.'
		elif self.is_the_board_full():
			return "Game over. It's a draw!"
		else:
			return 'not_over'


