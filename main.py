#!/usr/bin/env python3
from game import OXs
from utils import clear
from ai import ai

def main():
	
	do_you_want_to_play = True
	while do_you_want_to_play:
		clear()
		# Get user input
		print('''Welcome to Noughts and Crosses. A simple classic.
		Can you beat the computer in a grid-based battle?\n''')
		player_token = input('Choose a character to represent you on the board: ')
		ai_token = input('Choose a character to represent your opponent: ')
		
		# Set up the game
		game = OXs(player_token.upper()[0], ai_token.upper()[0])
		ai_player = ai()
		
		print('''HOW TO PLAY\n\n
		Enter a number from 1 to 9 to place your token 
		on the board.''')
		game.print_board_template()
		game.print_board()
		
		# Let's play!
		while game.game_over() == 'not_over':
			if game._current_marker == game._player_marker:
				# Player turn
				pos = input('Enter a number to take your turn: ')
				while not game.play_turn(pos):
					print('Try again' + pos + 'is not a valid position.')
					pos = input('Enter a number to take your turn: ')
				print(f'You chose position {pos}.')
			else:
				# AI turn
				print('It\'s my turn')
				ai_pos = ai_player.pick_a_spot(game)
				game.play_turn(ai_pos)
				print(f'I picked position {ai_pos}')

			# Print board again
			print('\n')
			game.print_board()

		# Game over
		print(game.game_over())
		print('\n')
		play_again = input('Do you want to play again? Y/N: ')
		if play_again[0] != 'y'.lower():
			do_you_want_to_play == False
		print('\n\n')

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
