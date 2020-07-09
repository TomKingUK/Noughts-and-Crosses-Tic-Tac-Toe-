#!/usr/bin/env python3
from game import OXs
from utils import clear

def main():
	
	do_you_want_to_play = True
	while do_you_want_to_play:
		clear()
		# TODO: Intro text
	
		print('Choose a character to represent you on the board')
		# TODO: user input [slice 1st char only]
		print('Choose a character to represent your opponent')
		# TODO: user input [slice 1st char only]

		game = OXs('X', 'O')
		game.print_board_template()
		game.print_board()
	

	


	# Logic tests for win line
	# print(game.is_there_a_winner())
	# print(f'Left diag: {game.left_diag()}')
	# print(f'Right diag: {game.right_diag()}')
	# print(f'Top row: {game.top_row()}')
	# print(f'Middle row: {game.middle_row()}')
	# print(f'Bottom row: {game.bottom_row()}')
	# print(f'First col: {game.first_col()}')
	# print(f'Second col: {game.second_col()}')
	# print(f'Last col: {game.last_col()}')

if __name__ == '__main__': main()
