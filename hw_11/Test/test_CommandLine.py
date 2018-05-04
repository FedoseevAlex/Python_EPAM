import unittest

from CommandLine import *

class TestCommandLine(unittest.TestCase):

    def test_get_help(self):
        """Check get_help function"""

        self.assertEqual(get_help(), 0.0, 'Test of Point().x failed. Returned value != 0.0')

if __name__ == '__main__':
    unittest.main()
