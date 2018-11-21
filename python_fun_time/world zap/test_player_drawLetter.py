"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import sys
if sys.version_info.major != 3:
    print('You must use Python 3.x version to run this unit test')
    sys.exit(1)

import unittest

import player

class TestPlayerDrawLetter(unittest.TestCase):
    def test001_exists(self):
        self.assertTrue('drawLetter' in dir(player.Player),
            'Function "drawLetter" is not defined, check your spelling')

    def test002_returnsString(self):
        from player import Player
        p = Player('Luke')
        letters = p.getLetters()
        newletter = p.drawLetter()
        self.assertTrue(isinstance(newletter, str), "You should have returned a string containing the new letter")
        self.assertEqual(len(newletter), 1, "You should have returned a single letter")

    def test003_updatesLetters(self):
        from player import Player
        p = Player('Luke')
        letters = p.getLetters()[:]
        newletter = p.drawLetter()
        newletters = p.getLetters()

        self.assertNotEqual(len(letters), len(newletters), "You should have updated the player's current letters")

        c = letters.count(newletter)
        c2 = newletters.count(newletter)
        self.assertEqual(c2, c+1, "You should added the new letter to the player's current list of letters")

    def test004_initUpdated(self):
        from player import Player
        p = Player('Luke')
        letters = p.getLetters()
        self.assertEqual(len(letters), 7, "The player should start out with 7 letters, update the constructor to give the player 7 random letters")


if __name__ == '__main__':
    unittest.main()
