#!/usr/bin/env python3
from os import system, name

# Clear the screen
def clear():
	_ = system('cls' if name == 'nt' else 'clear')
	

