import pygame

class Sun:

    def __init__( self, x, y, r ):
        self.mX = x
        self.mY = y
        self.mRadius = r
        return

    def draw( self, surface ):
        color = ( 255, 157, 0 )
        center = ( int( self.mX ), int( self.mY ) )
        pygame.draw.circle( surface, color, center, int( self.mRadius ), 0 )
        return

class Moon:

    def __init__( self, x, y, r ):
        self.mX = x
        self.mY = y
        self.mRadius = r
        return

    def draw( self, surface ):
        color = ( 0, 255, 255 )
        center = ( int( self.mX ), int( self.mY ) )
        pygame.draw.circle( surface, color, center, int( self.mRadius ), 0 )
        return
