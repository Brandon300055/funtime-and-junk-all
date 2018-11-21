import pygame

class Cloud:

    def __init__( self, x, y, w, h ):
        self.mX = x
        self.mY = y
        self.mWidth = w
        self.mHeight = h
        return

    def draw( self, surface ):
        color = ( 255, 255, 255 )
        rect = pygame.Rect( int( self.mX ), int( self.mY ), int( self.mWidth ), int( self.mHeight ) )
        pygame.draw.ellipse( surface, color, rect, 0 )
        return
