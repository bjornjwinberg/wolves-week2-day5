import sqlite3

class Board():
	def __init__(self):
		self.game_board = []

	def seed_game_board(self):
		for x in range(10):
			self.game_board.append("~" * 10)

	def print_board(self):
		for line in self.game_board:
			print (' '.join(line))

class Ship(self):
	def __init__(self):
		pass
