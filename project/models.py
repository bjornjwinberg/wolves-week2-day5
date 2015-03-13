import sqlite3

class Model:
	def __init__(self):
		pass

class Board:
	def __init__(self):
		self.board = []

	def seed_board(self):
		for x in range(10):
			self.board.append(" ~ "*10)

	def print_board(self):
		ocean = []
		print('   ', '    '.join([(str(x) + " ") for x in range(1,11)]))
		x = 65
		for row in self.board:
			print(chr(x), ' '.join(row))
			x+=1

new = Board()
new.seed_board()
new.print_board()
