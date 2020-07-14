#!/usr/bin/env python3
from game import EMPTY_MARKER
import random

class ai (object):
			
	def pick_a_spot(game):
		choices = []
		for i in range(len(game._board)):
			if game._board[i] != EMPTY_MARKER:
				choices.append(i)
		
		choice = random.randint(min(choices), max(choices))
		return choice
