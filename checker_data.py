import numpy as np 
from checkers_move import Checkers_move

class Checker_data:
	def __init__(self, rows=8, cols=8):
		self.rows = rows
		self.cols = cols
		self.empty = 0
		self.white = 1
		self.black = 2
		self.white_king = 3
		self.black_king = 4
		self.init_board()

	def init_board(self):
		self.board = np.zeros((self.rows, self.cols))
		# for row in range(self.rows):
		# 	for col in range(self.cols):
		# 		if row%2 == col%2:
		# 			if row<3:
		# 				self.board[row,col] = self.black
		# 			elif row>4:
		# 				self.board[row,col] = self.white
		# 			else:
		# 				self.board[row,col] = self.empty
		# 		else:
		# 			self.board[row,col] = self.empty
		self.board[4,2] = self.white
		self.board[3,3] = self.black
		self.board[1,5] = self.black

	def get_simple_player_moves(self, simple_player):
		moves = []

		simple_positions = self.get_simpte_positions(simple_player)

		if simple_player == self.white:
			for row, col in simple_positions:
				if self.can_jump_left(simple_player,row,col):
					moves.append(Checkers_move(row,col,row-2,col-2))
				if self.can_jump_right(simple_player,row,col):
					moves.append(Checkers_move(row,col,row-2,col+2))
			if len(moves)==0:
				for row, col in simple_positions:
					if self.can_move_left(simple_player,row,col):
						moves.append(Checkers_move(row, col, row-1, col-1))
					if self.can_move_right(simple_player,row,col):
						moves.append(Checkers_move(row, col, row-1, col+1))
		if simple_player == self.black:
			for row, col in simple_positions:
				if self.can_jump_left(simple_player,row,col):
					moves.append(Checkers_move(row,col,row+2,col-2))
				if self.can_jump_right(simple_player,row,col):
					moves.append(Checkers_move(row,col,row+2,col+2))
			if len(moves)==0:
				for row, col in simple_positions:
					if self.can_move_left(simple_player,row,col):
						moves.append(Checkers_move(row, col, row+1, col-1))
					if self.can_move_right(simple_player,row,col):
						moves.append(Checkers_move(row, col, row+1, col+1))

		return moves

	def get_simpte_positions(self, player):
		simple_positions = []
		for row in range(self.rows):
			for col in range(self.cols):
				if self.board[row,col] == player:
					simple_positions.append((row,col))
		return simple_positions

	def can_jump_left(self,simple_player,row,col):
		if simple_player == self.white:
			if col-2>-1 and row-2>-1 and self.board[row-1,col-1] == self.black and self.board[row-2,col-2] == self.empty:
				return True
			return False
		if simple_player == self.black:
			if col-2>-1 and row+2<8 and self.board[row+1,col-1] == self.white and self.board[row+2,col-2] == self.empty:
				return True
			return False

	def can_jump_right(self,simple_player,row,col):
		if simple_player == self.white:
			if col+2<8 and row-2>-1 and self.board[row-1,col+1] == self.black and self.board[row-2,col+2] == self.empty:
				return True
			return False
		if simple_player == self.black:
			if col+2<8 and row+2<8 and self.board[row+1,col+1] == self.white and self.board[row+2,col+2] == self.empty:
				return True
			return False

	def can_move_left(self,simple_player,row,col):
		if simple_player == self.white:
			if col-1>-1 and self.board[row-1,col-1] == self.empty:
				return True
			return False
		if simple_player == self.black:
			if col-1>-1 and self.board[row+1,col-1] == self.empty:
				return True
			return False

	def can_move_right(self,simple_player,row,col):
		if simple_player == self.white:
			if col+1<8 and self.board[row-1, col+1] == self.empty:
				return True
			return False
		if simple_player == self.black:
			if col+1<8 and self.board[row+1, col+1] == self.empty:
				return True
			return False

	def make_move(self,simple_player,r1,c1,r2,c2):
		if simple_player == self.white:
			simple_moves = self.get_simple_player_moves(simple_player)
			simple_moves2 = []
			for pos in simple_moves:
				simple_moves2.append((pos.from_row,pos.from_col,pos.to_row,pos.to_col))
			if (r1,c1,r2,c2) in simple_moves2:
				self.board[r2,c2] = self.board[r1,c1]
				self.board[r1,c1] = self.empty
				if r1-r2 == 2 or r1-r2 == -2:
					eatr = int((r1+r2)/2)
					eatc = int((c1+c2)/2)
					self.board[eatr,eatc] = self.empty
				if r2==0 and self.board[r2,c2] == self.white:
					self.board[r2,c2] = self.white_king
			else:
				print("invalid move")

		elif simple_player == self.black:
			simple_moves = self.get_simple_player_moves(simple_player)
			simple_moves2 = []
			for pos in simple_moves:
				simple_moves2.append((pos.from_row,pos.from_col,pos.to_row,pos.to_col))
			if (r1,c1,r2,c2) in simple_moves2:
				self.board[r2,c2] = self.board[r1,c1]
				self.board[r1,c1] = self.empty
				if r1-r2 == 2 or r1-r2 == -2:
					eatr = int((r1+r2)/2)
					eatc = int((c1+c2)/2)
					self.board[eatr,eatc] = self.empty
				if r2==7 and self.board[r2,c2] == self.black:
					self.board[r2,c2] = self.black_king
			else:
				print("invalid move")