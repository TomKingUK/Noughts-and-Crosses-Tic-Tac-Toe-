#!/usr/bin/env python3
from game import EMPTY_MARKER
import random

class ai (object):
			
	def pick_a_spot(self, game):
		choices = []
		for i in range(len(game._board)):
			if game._board[i] == EMPTY_MARKER:
				choices.append(i)
		print('Choices:', choices)
		choice = random.randint(min(choices), max(choices))
		print('Choice: ', choice)
		return choice + 1
