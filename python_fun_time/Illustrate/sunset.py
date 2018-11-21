import sun, sky, cloud, mountain, smallbird
import pygame

class Star:

    def __init__( self, x, y, r ):
        self.mX = x
        self.mY = y
        self.mRadius = r
        return

    def draw( self, surface ):
        color = ( 255, 255, 255 )
        center = ( int( self.mX ), int( self.mY ) )
        pygame.draw.circle( surface, color, center, int( self.mRadius ), 0 )
        return


class Sunset:

    def __init__( self, width, height ):
        self.mSky = sky.Sky( 1000, 800 )
        self.mSun = sun.Sun( 400, 200, 110 )
        self.mCloud1 = cloud.Cloud( 50, 150, 255, 95 )
        self.mCloud2 = cloud.Cloud( 650, 110, 310, 88 )
        ground = [ ( 1000, 800), ( 0,800 ), ( 0, 450 ),  ( 1000, 450 )]
        grass = ( 96, 128, 56 )

        houseColor = ( 96, 100, 76 )
        house = [ ( 0, 450), ( 450,450 ), ( 450, 450 ),  ( 0, 450 ) ]
        self.mSmallBird = smallbird.SmallBird( 100, 200, 50, 15 )
        self.mMountain = mountain.Mountain( ground, grass)
        self.house = mountain.Mountain( house, houseColor)
        return

    def draw( self, surface ):
        self.mSky.draw( surface )
        self.mSun.draw( surface )
        self.mCloud1.draw( surface )
        self.mCloud2.draw( surface )
        self.house.draw( surface )
        self.mMountain.draw( surface )

        return
