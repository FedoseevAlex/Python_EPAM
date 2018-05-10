"""
This file contains logic for similar_files script.
Functions:
    similar(**kwargs) -> dict
    Find all files and calculate hashes based on file contents. Compose files and hashes into dict and remove
    unique files.
    Return dict, where:
    keys: file hashes, values: paths to similar files

    print_work(duplicates: dict) -> None
    Prints non unique files by groups that contains of similar files.
"""
import os
from contextlib import closing

def similar(**kwargs):
    """
    Entry point for similar_files script.
    This function handles hash calculation of all files found in requested directory (if -r option is enabled
    then also in subdirectories). Hash calculated from file contents. After that duplicate files are printed.

    :param kwargs: Command line options got from user as keywords. Contains directory to find and other options.
    :type kwargs: dict
    :return: dict -- keys: file hashes, values: paths to similar files
    """
    # Create directory paths generator
    dirpath_generator = os.walk(kwargs['directory'])
    index_files = dict()
    while True:
        # Get next value from dirnames_generator
        try:
            contents = next(dirpath_generator)
        except StopIteration:
            break
        else:
            current_dir, sub_dirs, files = contents

        for file in files:
            file_path = os.path.join(current_dir, file)
            with closing(open(file_path, 'rb')) as f:
                short_path = os.path.join(os.path.basename(current_dir), file)
                file_hash = hash(f.read())
                if file_hash in index_files.keys():
                    index_files[file_hash].append(short_path)
                else:
                    index_files[file_hash] = [short_path, ]
        # Exit if -r flag is not present
        if not kwargs['recursively']:
            break
    for key in index_files.copy().keys():
        if len(index_files[key]) < 2:
            index_files.pop(key)

    print_work(index_files)
    return index_files

def print_work(duplicates: dict):
    """
    Handles output for user.

    :param duplicates: Contains groups of similar files by file hash.
    :type duplicates: dict -- keys: file hash, values: list of similar files
    :return: None
    """
    if duplicates:
        print('Duplicate files found:\n')
        for index, files in enumerate(duplicates.values(), start=1):
            print('\tSimilar group {}\n'.format(index))
            print(*files, sep='\n')
            print(r'*' * 30, end='\n\n')
    else:
        print('No similar files found!')

