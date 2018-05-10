#!/usr/bin/env python3.6
"""
Image downloader module. Contains all required logic to download images from file with url's and resize them.
"""

import argparse
import os
import requests
from multiprocessing.pool import ThreadPool
from io import BytesIO
from threading import Lock
from time import time

from PIL import Image

# request_errors - errors during downloading
# process_errors - number of processing errors
# bytes - total amount
# downloaded - count downloaded files
# requested - how many files were requested to download
REPORT = dict(request_errors=0, process_errors=0, bytes=0, downloaded=0, requested=0)
REP_LOCK = Lock()


class ExistenceCheck(argparse.Action):
    """
    Custom action for argparse. This class check file existence and
    raises argparse.ArgumentParser(...).error if
    requested file does not exist.
    """
    def __call__(self, parser, namespace, values, option_string=None):
        """
        To use custom action it is mandatory to redefine __call__ method.
        Here we check file existence. If file is not present parser error raised.
        If such file exists just go through.

        :param parser: This is argparse.ArgumentParser object which use this action.
        :param namespace: Namespace of parser. Contains all arguments from command line.
        :param values: Here stored argument value.
        :param option_string: String representation of argument name.
        :return: None
        """
        if not os.path.exists(values):
            parser.error('Requested file does not exist!')
        else:
            setattr(namespace, self.dest, values)


class SizeExtractor(argparse.Action):
    """
    Custom action for argparse. This class convert picture size given like '128x128' to a tuple (128, 128).
    """
    def __call__(self, parser, namespace, values, option_string=None):
        """
        This method verifies input string to match pattern '[length]x[width]' and converts string to tuple.

        :param parser: This is argparse.ArgumentParser object which use this action.
        :param namespace: Namespace of parser. Contains all arguments from command line.
        :param values: Here stored argument value.
        :param option_string: String representation of argument name.
        :return: None
        """
        try:
            height, width = values.casefold().split('x')
            height = int(height)
            width = int(width)
        except ValueError:
            parser.error('Wrong --size argument. Must be like [number]x[number] e.g. 128x128.')
        else:
            setattr(namespace, self.dest, tuple([height, width]))


def download():
    """
    Entry point for download.py. Unites all necessary logic for downloading and resizing images.
    Command line parameters:
        file - text file with URL's to download images.
        --dir - directory to save resized images to.
        --threads - how many threads to invoke for downloading.
        --size - height and width of output images

    :return: None
    """
    time_start = time()
    # Setting up parser
    parser = argparse.ArgumentParser(usage='download.py [OPTIONS] file')

    parser.add_argument('file', type=str, help="A file with url's to download.", action=ExistenceCheck)
    parser.add_argument('--dir', default='.', type=str, help='Directory to store download images.')
    parser.add_argument('--threads', default=1, type=int, help='Number of threads to process download.')
    parser.add_argument('--size', default=(128, 128, ), help='Size of downloaded pictures.', action=SizeExtractor)

    # Get dict from parsed args
    args = vars(parser.parse_args())

    # Get lines from requested file
    url_list = get_lines(args['file'])
    if not url_list:
        print("No URL's to download.")
        return

    # Save URL's count in REPORT
    REPORT['requested'] = len(url_list)

    # Make directory to store downloaded images
    os.makedirs(args['dir'], exist_ok=True)

    # Create thread pool and wait downloading to finish
    pool = ThreadPool(args['threads'])

    thread_arguments = [(index, url, args['size'], args['dir']) for index, url in enumerate(url_list)]

    pool.map(thread_work, thread_arguments)

    pool.close()
    pool.join()

    print_report(time() - time_start)


def get_lines(file: str) -> list:
    """
    Split file contents line by line and return all lines as list.

    :param file: file path
    :type file: str
    :return: list with lines from file
    """
    lines = list()
    try:
        f = open(file, 'r')
    except IOError:
        print('Could not read file.')
    else:
        lines = f.read().splitlines()
        f.close()
    return lines


def thread_work(params: tuple) -> bool:
    """
    This function handle work sequence for one thread.
    Work sequence contains downloading files from internet and add information to report.

    :param params: contains image index according to number line in file and url.
    :type params: tuple -- (index: int, url: str)
    :return: bool -- True if no errors occured, False otherwise.
    """
    index, url, size, dir = params
    img = None
    # Download image
    try:
        # Added header to avoid http 403 error. Servers so clever now that they block requests from programs.
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    except requests.ConnectionError:
        REP_LOCK.acquire()
        REPORT['request_errors'] += 1
        REP_LOCK.release()
        print('Error during downloading image {}.'.format(index))
        return False

    img = response.content
    bytes_load = len(img)
    REP_LOCK.acquire()
    REPORT['downloaded'] += 1
    REPORT['bytes'] += bytes_load
    REP_LOCK.release()
    response.close()
    print('Image {} finished downloading. Size: {} bytes'.format(index, bytes_load))

    img_path = os.path.join(dir, str(index).zfill(5))
    try:
        image = Image.open(BytesIO(img))
    except (TypeError, OSError):
        print('Error occurred during {} image resize. File not created!'.format(index))
        REPORT['process_errors'] += 1
        return False

    image.thumbnail(size)
    image.save(img_path + '.jpg', "JPEG")
    return True


def print_report(runtime: float):
    """
    Report printing.

    :param runtime: time of program spent to do it's business.
    :type runtime: float
    :return: None
    """
    print('Report:')
    print('\tDownload: {} bytes ({:.2f} kbytes) '.format(REPORT['bytes'], REPORT['bytes'] / 1024))
    print('\tTotal files downloaded: {}/{}'.format(REPORT['downloaded'], REPORT['requested']))
    print('\tDownload errors: {}'.format(REPORT['request_errors']))
    print('\tImage processing errors: {}'.format(REPORT['process_errors']))
    print('\tFiles saved: {}'.format(REPORT['requested'] - REPORT['request_errors'] - REPORT['process_errors']))
    print('Elapsed time - {:.2f} s'.format(runtime))


if __name__ == '__main__':
    download()
