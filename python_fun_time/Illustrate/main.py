import pygame
import game
# YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
import sunset

# YOU SHOULD CONFIGURE THESE TO MATCH YOUR GAME
# window title bar text
TITLE = "Sunset"
# pixels width
WINDOW_WIDTH  = 1000
# pixels high
WINDOW_HEIGHT = 800
# frames per second
DESIRED_RATE  = 2

class PygameApp( game.Game ):

    def __init__( self, title, width, height, frame_rate ):

        game.Game.__init__( self, title, width, height, frame_rate )

        self.mGame = sunset.Sunset( width, height )
        return


    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):

        x = mouse_position[ 0 ]
        y = mouse_position[ 1 ]


        return

    def paint( self, surface ):
        # Draw the current state of the game instance
        self.mGame.draw( surface )
        return

def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )

if __name__ == "__main__":
    main( )
