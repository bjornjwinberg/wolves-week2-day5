from models import *
from views import *

class Battleship:
	def __init__(self):
		self.view = View()
		self.board = Gameboard()
		self.player = Player()
		self.ship = Ship()

	def start_menu(self):
		self.view.welcome_first()
		first_player = self.view.first_player()
		second_player = self.view.second_player()
		first_player_ship = self.view.select_ship()
		second_player_ship = self.view.select_ship()

	def deploy(self):
		ship_length = eval(self.view.ship_choice())
		

battleship = Battleship()
battleship.start_menu()
