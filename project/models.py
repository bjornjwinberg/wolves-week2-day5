import sqlite3

class Gameboard:
	def __init__(self):
		self.board = []

	def seed_board(self):
		for x in range(10):
			self.board.append(" ~ "*10)

	def print_board(self):
		print('   ', '    '.join([(str(x) + " ") for x in range(1,11)]))
		x = 65
		for row in self.board:
			print(chr(x), ' '.join(row))
			print()
			x+=1

new = Gameboard()
new.seed_board()
new.print_board()
