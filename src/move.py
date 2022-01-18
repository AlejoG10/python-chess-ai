from const import *

class Move:
    '''
        Stores a game move data
    '''

    def __init__(self, initial, final):
        self.initial = initial # BoardPos
        self.final = final # BoardPos

    def __str__(self):
        return str(self.initial) + ', ' + str(self.final)

    def __eq__(self, other):
        return self.initial == other.initial and self.final == other.final