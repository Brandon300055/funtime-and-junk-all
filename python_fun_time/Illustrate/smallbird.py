import pygame
import math

class SmallBird:

    def __init__( self, x, y, w, h ):
        self.mX = x
        self.mY = y
        self.mWidth = w
        self.mHeight = h
        return

    def draw( self, surface ):
        color = ( 0, 0, 0 )
        rect = pygame.Rect( int( self.mX ), int( self.mY ), int( self.mWidth / 2 ), int( self.mHeight * 2 ) )
        start_angle = math.radians( 0 )
        stop_angle = math.radians( 180 )
        width = 3
        pygame.draw.arc( surface, color, rect, start_angle, stop_angle, width )

        rect = pygame.Rect( int( self.mX + self.mWidth/2 ), int( self.mY ), int( self.mWidth / 2 ), int( self.mHeight * 2 ) )
        pygame.draw.arc( surface, color, rect, start_angle, stop_angle, width )

        return
