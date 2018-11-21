import pygame

class Sky:

    def __init__( self, width, height ):
        self.mWidth = width
        self.mHeight = height
        return

    def draw( self, surface ):
        color = ( 0, 0, 200 )
        rect = pygame.Rect( 0, 0, int( self.mWidth ), int( self.mHeight ) )
        pygame.draw.rect( surface, color, rect, 0 )
        return
