#!/usr/bin/env python3
from game import OXs
from utils import clear

def main():
	game = OXs('X', 'O')
	print(game._board)
	clear()
	print(game.within_range(1))
	for i in range(len(game._board)):
		print(game.is_occupied(i+1))
	game.print_board()
	game.print_board_template()

if __name__ == '__main__': main()
