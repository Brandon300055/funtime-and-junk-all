import pygame

class House:

    def __init__( self, outline, color ):
        self.mOutline = outline
        self.color = color
        return

    def draw( self, surface ):
        pygame.draw.polygon( surface, self.color, self.mOutline, 0 )
        return
