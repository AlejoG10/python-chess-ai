from const import *

class Square:

    ALPHACOLS = { 0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h' }

    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece
        self.alphacol = self.ALPHACOLS[col]

    def __str__(self):
        return '(' + str(self.row) + ', ' + str(self.col) + ')'

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    # -------------
    # OTHER METHODS
    # -------------

    def has_piece(self):
        return self.piece != None

    def has_team_piece(self, color):
        return self.piece != None and self.piece.color == color

    def has_rival_piece(self, color):
        return self.piece != None and self.piece.color != color
    
    def isempty(self):
        return self.piece == None

    def isempty_or_rival(self, color):
        return self.piece == None or self.piece.color != color

    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg > 7: return False
        return True
    
    @staticmethod
    def get_alphacol(col):
        alphacols = { 0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h' }
        return alphacols[col]