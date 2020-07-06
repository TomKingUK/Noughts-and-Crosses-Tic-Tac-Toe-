#!/usr/bin/env python3

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
		board = ['*'] * 9
		return board
		
	def play_turn(self, pos) -> bool:
		is_valid = self.within_range(pos) and not self.is_occupied(pos)
		if is_valid:
			self._board[pos-1] = self._current_marker
			# Flip the turn from ai to player, or player to ai
			self._current_marker = self._ai_marker if self._player_marker else self._player_marker
		return is_valid # Allows us to check if turn was valid

	# Check if a played turn is within range (1-9)
	def within_range(self, number):
		return 0 < number <= len(self._board)

	def is_occupied(self, pos):
		return self._board[pos-1] != '*'
	