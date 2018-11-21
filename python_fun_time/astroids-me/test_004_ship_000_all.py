"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
Do Not Move on to the next function until its tests report 'ok' or your code
may not work as expected.
"""

import unittest

def suite( ):
    test_modules = [ 
        "test_004_ship_001_constructor_and_getters",
        "test_004_ship_002_evolve",
    ]

    s = unittest.TestSuite( )
    for m in test_modules:
        s.addTest( __import__(m ).suite( ) )
        
    return s
        
if __name__ == '__main__':
    runner = unittest.TextTestRunner( )
    runner.run( suite( ) )