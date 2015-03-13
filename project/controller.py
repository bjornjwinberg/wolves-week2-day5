from models import *
from views import *

class Battleship:
	def __init__(self):
		self.view = View()
		self.board = Gameboard()
		self.p1 = self.view.first_player()
		self.p2 = self.view.second_player()

	def start_menu(self):
		self.view.welcome()
		self.player1 = Player(self.p1)
		self.player2 = Player(self.p2)

	def deploy(self):
		player_ship = self.view.select_ship()
		second_player_ship = self.view.select_ship()
		self.p1.board.print_board()
		self.p2.board.print_board()

	# def deploy(self):
	# 	ship_length = eval(self.view.ship_choice())


battleship = Battleship()
battleship.start_menu()
battleship.deploy()
