import pygame
import game
from config import *

class Frogger( game.Game ):

    def __init__( self, title, width, height, frame_rate ):

        game.Game.__init__( self, title, width, height, frame_rate )
        self.stage1 = froggerlib.Stage(0, 10 * VG, SCREEN_WIDTH, VG)
        # create a game instance
        # YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
        self.mGame = example.Example( width, height )
        return


    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):
        # keys contains all keys currently held down
        # newkeys contains all keys pressed since the last frame
        # Use pygame.K_? as the keyboard keys.
        # Examples: pygame.K_a, pygame.K_UP, etc.
        # if pygame.K_UP in newkeys:
        #    The user just pressed the UP key
        #
        # buttons contains all mouse buttons currently held down
        # newbuttons contains all buttons pressed since the last frame
        # Use 1, 2, 3 as the mouse buttons
        # if 3 in buttons:
        #    The user is holding down the right mouse button
        #
        # mouse_position contains x and y location of mouse in window
        # dt contains the number of seconds since last frame

        x = mouse_position[ 0 ]
        y = mouse_position[ 1 ]

        # Update the state of the game instance
        # YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
        if pygame.K_a in newkeys:
            self.mGame.actOnPressA( )
        elif pygame.K_a in keys:
            self.mGame.actOnHoldA( )

        if pygame.K_UP in keys:
            self.mGame.actOnHoldUP( )

        if 1 in newbuttons:
            self.mGame.actOnLeftClick( x, y )

        self.mGame.evolve( dt )

        return

    def draw_stage(self,stage):
        color = (212,144,210)
        rect = pygame.Rect(stage.getX(), setage.getY(), stage.getWidth(), stage.getHeight())

    def paint( self, surface ):
        # Draw the current state of the game instance
        self.mGame.draw( surface )

        if DEBUG:
            for y in range(ROWS):

        return

def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )

if __name__ == "__main__":
    main( )
