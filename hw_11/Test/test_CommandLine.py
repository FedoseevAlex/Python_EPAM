import unittest
from unittest.mock import patch

from CommandLine import *
from Triangle import Point, Triangle

class TestCommandLine(unittest.TestCase):
    """
    Class for testing functions in CommandLine module.
    """

    @patch('builtins.input', return_value='help')
    def test_get_help(self):
        """Check output of get_help function."""
        help_string = """
Help:
    new -- Command to define triangle from three points.
    help -- Show help message. Possible alternatives are: '?', 'h'.
    quit -- Quit and close program. Possible alternatives are: 'q', 'exit'.
    area -- Calculate and print area of triangle.
    isosceles -- Print True if given triangle is isosceles, or False otherwise.
    equilateral -- Print True if given triangle is equilateral, or False if not."""
        self.assertEqual(get_help(), help_string, 'Test of get_help() failed. Returned value != help string')


    #






if __name__ == '__main__':
    unittest.main()
