"""
Tests for similar_files script.
"""
import argparse
import os
import shutil
import unittest
from itertools import cycle

from SuperTool import find

TMP_DIR = os.path.join(os.path.dirname(__file__), 'tmp')


class TestFindSimilar(unittest.TestCase):

    def setUp(self):
        """
        Generates temporary files to test similar_files script.

        :return: None
        """
        if os.path.exists(TMP_DIR):
            shutil.rmtree(TMP_DIR)
        file_names = [letter + '.txt' for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']]
        file_contents = ['test data 1', 'test data 2', 'test data 3', 'test data 3',
                         'test data 1', 'test data 2', 'test data 1', 'test data 4']
        os.makedirs(TMP_DIR)

        subdir_paths = [os.path.join(TMP_DIR, name) for name in ['subdir1', 'subdir2']]
        subdir_paths.append(TMP_DIR)
        os.makedirs(os.path.join(TMP_DIR, subdir_paths[0]))
        os.makedirs(os.path.join(TMP_DIR, subdir_paths[1]))
        dirs = cycle(subdir_paths)

        for index, file in enumerate(file_names):
            f = open(os.path.join(next(dirs), file), 'w')
            f.write(file_contents[index])
            f.close()

    @staticmethod
    def make_parser(argv):
        """
        Setting up parser and parse argv which is a list of command line arguments mocking sys.argv.

        :param argv: list of strings
        :return: parser Namespace object
        """
        parser = argparse.ArgumentParser(description='Find similar files.', usage='similar_files [options] directory')

        parser.add_argument('directory', type=str, help='Target directory')
        parser.add_argument('-r', '--recursively', help='Check subdirectories for similar files',
                            action='store_true')
        return parser.parse_args(argv)

    def test_no_similar_files(self):
        """Positive testing src/test/tmp -> no similar files."""
        args = vars(self.make_parser([TMP_DIR]))
        res = list(find.similar(**args).values())
        self.assertListEqual(res, [])

    def test_similar_files(self):
        """Positive testing src/test/tmp/subdir1"""
        args = vars(self.make_parser([os.path.join(TMP_DIR, 'subdir1')]))
        res = find.similar(**args)
        self.assertListEqual(list(res.values())[0], ['subdir1/a.txt', 'subdir1/g.txt'])

    def test_similar_files_recursive(self):
        """Positive testing with -r option src/test/tmp"""
        args = vars(self.make_parser(['-r', TMP_DIR]))
        res = find.similar(**args)
        self.assertListEqual(list(res.values()), [['tmp/f.txt', 'subdir2/b.txt'], ['tmp/c.txt', 'subdir1/d.txt'],
                                                  ['subdir2/e.txt', 'subdir1/a.txt', 'subdir1/g.txt']])


    def tearDown(self):
        shutil.rmtree(TMP_DIR)


if __name__ == '__main__':
    unittest.main()