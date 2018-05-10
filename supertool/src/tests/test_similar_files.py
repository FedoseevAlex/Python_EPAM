"""
Tests for similar_files script
"""
import os
import unittest

from SuperTool import find

TMP_DIR = os.path.join(os.path.dirname(__file__), 'tmp')


class TestFindSimilar(unittest.TestCase):

    def test_generate_files_for_test(self):
        if os.path.exists(TMP_DIR):
            os.removedirs(TMP_DIR)

        os.makedirs(TMP_DIR)
        os.makedirs(os.path.join(TMP_DIR, 'subdir1'))
        os.makedirs(os.path.join(TMP_DIR, 'subdir2'))
        os.makedirs(os.path.join(TMP_DIR, 'subdir3'))

    def test_no_similar_files(self):
        pass


if __name__ == '__main__':
    unittest.main()