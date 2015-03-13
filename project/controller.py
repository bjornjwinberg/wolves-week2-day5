from models import *
from views import *

class Battleship:
	def __init__(self):
		self.view = View()
		self.board = Gameboard()
		self.player1 = Player(self.view.first_player())
		self.player2 = Player(self.view.second_player())

	def run(self):
		self.p1_deploy()
		self.p2_deploy()

	def p1_deploy(self):
		self.view.show_sea(self.player1.name)
		self.player1.board.print_board()
		player1_ship = self.view.select_ship()
		player1_bow = self.view.starting_point_of_ship()
		player1_orientation = self.view.select_positioning()

	# def p2_deploy(self):
	# 	self.player2.board.print_board()
	# 	player2_ship = self.view.select_ship(self.player2)
	# 	player2_bow = self.view.starting_point_of_ship()
	# 	player2_orientation = self.view.select_positioning()


	# def deploy(self):
	# 	ship_length = eval(self.view.ship_choice())

Battleship().run()
# battleship.p1_deploy()
# battleship.p2_deploy()
