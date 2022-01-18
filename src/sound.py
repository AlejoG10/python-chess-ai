import pygame

class Sound:
    '''
        Stores the game sounds
    '''
    
    def __init__(self, path):
        self.path = path
        self.sound = pygame.mixer.Sound(path)

    # -------------
    # CLASS METHODS
    # -------------

    def play(self):
        pygame.mixer.Sound.play(self.sound)