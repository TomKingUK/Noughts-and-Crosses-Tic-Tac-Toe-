#!/usr/bin/env python3
from game import OXs
from utils import clear
from ai import ai
from time import sleep

def main():
	
	do_you_want_to_play = True
	while do_you_want_to_play:
		clear()
		# Get user input
		
		print('Welcome to Noughts and Crosses.\n\
A simple text-based version of a classic.\n\n\
Can you beat the computer in a grid-based battle?\n')
		player_token = input('Choose a character to represent you on the board: ')
		ai_token = input('Choose a character to represent the computer: ')
		
		# Set up the game
		game = OXs(player_token.upper()[0], ai_token.upper()[0])
		ai_player = ai()
		clear()
		print('\n\nHOW TO PLAY\n\
Enter a number from 1 to 9 to place your token \
on the board.')
		game.print_board_template()
		input("Press ENTER to continue...")
		# Let's play!
		print('\nLet\'s play!')
		sleep(1.5)
		clear()
		game.print_board()
		while game.game_over() == 'not_over':
			if game._current_marker == game._player_marker:
				# Begin player turn
				try:
					# TODO: Create reusable input function
					pos = int(input('Enter a number [1-9] to take your turn: '))
				except:
					# TODO: Implement proper error handling
					print('Invalid input. Enter an inter from 1 to 9.')
					pos = int(input('Enter a number [1-9] to take your turn: '))
				# Play turn
				while not game.play_turn(pos):
					print(f'Try again {pos} is not a valid position.')
					pos = int(input('Enter a number [1-9] to take your turn: '))
					print(f'You chose position {pos}.')
			else:
				# Begin AI turn
				# clear()
				print('AI: It\'s my turn... ', flush=True, end='')
				ai_pos = ai_player.pick_a_spot(game)
				sleep(2)
				# Play AI turn
				game.play_turn(ai_pos)
				print(f'I pick position {ai_pos}')
				sleep(1)
					
			# Print board again
			print('\n')
			clear()
			game.print_board()
			sleep(0.5)

		# Game over
		print(game.game_over())
		print('\n')
		input('Press ENTER to play again...')
		
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
