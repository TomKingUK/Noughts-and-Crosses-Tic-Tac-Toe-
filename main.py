#!/usr/bin/env python3
from game import OXs

def main():
	game = OXs('X', 'O')
	
	print(game._board)
	print(game.within_range(1))
	for i in range(len(game._board)):
		print(game.is_occupied(i+1))

if __name__ == '__main__': main()
