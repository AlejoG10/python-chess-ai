import os

class Piece:
    '''
        Creates the game pieces
    '''

    def __init__(self, name, color, value, texture_rect=None):
        value_sign = 1 if color == 'white' else -1
        self.name = name
        self.color = color
        self.value = value * value_sign
        self.moved = False
        self.moves = []
        self.set_texture()
        self.texture_rect = texture_rect

    def __str__(self):
        return self.color[0] + self.name[0].upper() + self.name[1].upper()

    # -------------
    # CLASS METHODS
    # -------------

    def add_move(self, move):
        self.moves.append(move)

    def set_texture(self, size=80):
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png')


class Pawn(Piece):
    '''
        Creates the pawns
    '''

    def __init__(self, color):
        self.dir = -1 if color == 'white' else 1
        super().__init__('pawn', color, 1.0)

class Knight(Piece):
    '''
        Creates the knights
    '''

    def __init__(self, color):
        super().__init__('knight', color, 3.0)

class Bishop(Piece):
    '''
        Creates the bishops
    '''

    def __init__(self, color):
        super().__init__('bishop', color, 3.001)

class Rook(Piece):
    '''
        Creates the rooks
    '''

    def __init__(self, color):
        super().__init__('rook', color, 5.0)

class Queen(Piece):
    '''
        Creates the queens
    '''

    def __init__(self, color):
        super().__init__('queen', color, 9.0)

class King(Piece):
    '''
        Creates the kings
    '''

    def __init__(self, color):
        super().__init__('king', color, 10000.0)