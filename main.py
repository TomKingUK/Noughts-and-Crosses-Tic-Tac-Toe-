#!/usr/bin/env python3
from game import OXs
from utils import clear

def main():
	game = OXs('X', 'O')
	clear()
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
