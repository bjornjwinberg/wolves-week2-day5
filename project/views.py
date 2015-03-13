import blessings

t = terminal()

class View:
	def __init__(self):
		pass

	def welcome_first(self):
		print("Welcome to Battleship.  Hope you brought a life-jacket.  Enter player 1 name: ")
		return input()

	def welcome_second(self):
		print("Enter Player2 name:  ")
		return input()
