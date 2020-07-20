#!/usr/bin/env python3
from game import EMPTY_MARKER
import random

class ai (object):
			
	def pick_a_spot(self, game):
		choices = []
		for i in range(len(game._board)):
			if game._board[i] == EMPTY_MARKER:
				choices.append(i)
		choice = choices[random.randint(0, len(choices)-1)]
		return choice + 1
